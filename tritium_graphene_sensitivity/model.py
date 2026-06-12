from __future__ import annotations

from collections import OrderedDict
import threading

import numpy as np
from scipy.signal import fftconvolve

from .configs import SECONDS_PER_YEAR, SimulationConfig
from .response import bin_density_interpolated, gaussian_kernel, pileup_density
from .spectra import (
    blocking_acceptance,
    make_endpoint_grid,
    normalize_density,
    tritium_endpoint_spectrum,
)


_MODEL_CACHE_MAX = 16
_MODEL_CACHE: OrderedDict[tuple, dict] = OrderedDict()
_MODEL_CACHE_LOCK = threading.RLock()


def _model_cache_key(config: SimulationConfig, mnu2_ev2: float | None) -> tuple:
    return (
        float(config.endpoint_energy_ev),
        float(config.mnu2_ev2 if mnu2_ev2 is None else mnu2_ev2),
        float(config.detector_fwhm_ev),
        float(config.zero_point_fwhm_ev),
        float(config.blocking_fraction),
        int(config.n_detectors),
        float(config.activity_bq),
        float(config.tau_eff_us),
        float(config.background_per_ev_year),
        int(config.n_grid),
        int(config.n_bins),
        float(config.fit_low_offset_ev),
        float(config.fit_high_offset_ev),
    )


def build_model(config: SimulationConfig, mnu2_ev2: float | None = None) -> dict:
    cache_key = _model_cache_key(config, mnu2_ev2)
    with _MODEL_CACHE_LOCK:
        cached = _MODEL_CACHE.get(cache_key)
        if cached is not None:
            _MODEL_CACHE.move_to_end(cache_key)
            return cached

    model = _build_model_uncached(config, mnu2_ev2=mnu2_ev2)

    with _MODEL_CACHE_LOCK:
        _MODEL_CACHE[cache_key] = model
        _MODEL_CACHE.move_to_end(cache_key)
        while len(_MODEL_CACHE) > _MODEL_CACHE_MAX:
            _MODEL_CACHE.popitem(last=False)
    return model


def _gaussian_convolve_preserve_area(
    energy_ev: np.ndarray, density: np.ndarray, fwhm_ev: float
) -> np.ndarray:
    if fwhm_ev <= 0.0:
        return np.asarray(density, dtype=float)
    d_e = float(energy_ev[1] - energy_ev[0])
    kernel = gaussian_kernel(d_e, fwhm_ev / 2.355)
    return np.clip(fftconvolve(density, kernel, mode="same"), 0.0, None)


def _build_model_uncached(config: SimulationConfig, mnu2_ev2: float | None = None) -> dict:
    endpoint = float(config.endpoint_energy_ev)
    energy = make_endpoint_grid(endpoint, int(config.n_grid))
    mnu2 = float(config.mnu2_ev2 if mnu2_ev2 is None else mnu2_ev2)

    beta_density = tritium_endpoint_spectrum(
        energy,
        endpoint,
        mnu2,
    )
    source_density = _gaussian_convolve_preserve_area(
        energy, beta_density, config.zero_point_fwhm_ev
    )
    source_density = normalize_density(energy, source_density)
    acceptance = blocking_acceptance(energy, float(config.blocking_voltage_ev), True)
    accepted_single = source_density * acceptance
    accepted_fraction = float(np.trapezoid(accepted_single, energy))

    single_measured = _gaussian_convolve_preserve_area(
        energy, accepted_single, config.detector_fwhm_ev
    )

    f_pp = np.clip(config.pileup_fraction, 0.0, 0.25)
    if f_pp > 0.0 and accepted_fraction > 0.0:
        pp_energy, pp_norm = pileup_density(energy - energy[0], normalize_density(energy, accepted_single))
        pp_energy = pp_energy + 2.0 * energy[0]
        pp_on_grid = np.interp(energy, pp_energy, pp_norm, left=0.0, right=0.0)
        pileup_measured = _gaussian_convolve_preserve_area(
            energy, pp_on_grid * accepted_fraction**2, config.detector_fwhm_ev
        )
    else:
        pp_on_grid = np.zeros_like(energy)
        pileup_measured = np.zeros_like(energy)

    measured = (1.0 - f_pp) * single_measured + f_pp * pileup_measured

    if config.background_per_ev_year > 0.0:
        bg_per_sim_event = config.background_per_ev_year / max(
            config.total_rate_hz * SECONDS_PER_YEAR, 1.0
        )
        measured = measured + bg_per_sim_event

    low = max(energy[0], endpoint + config.fit_low_offset_ev)
    high = min(energy[-1], endpoint + config.fit_high_offset_ev)
    if high <= low:
        raise ValueError("Fit window is empty. Check endpoint and fit offsets.")
    bin_edges = np.linspace(low, high, config.n_bins + 1)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    bin_probs = bin_density_interpolated(energy, measured, bin_edges)
    single_bin_probs = (1.0 - f_pp) * bin_density_interpolated(
        energy, single_measured, bin_edges
    )
    pileup_bin_probs = f_pp * bin_density_interpolated(energy, pileup_measured, bin_edges)

    return {
        "energy_ev": energy,
        "single_density": accepted_single,
        "raw_beta_density": beta_density,
        "source_density": source_density,
        "acceptance": acceptance,
        "accepted_fraction_in_window": accepted_fraction,
        "total_accepted_fraction": accepted_fraction,
        "pileup_density": pp_on_grid,
        "single_measured_density": single_measured,
        "pileup_measured_density": pileup_measured,
        "passing_pileup_density": f_pp * pileup_measured,
        "measured_density": measured,
        "bin_edges_ev": bin_edges,
        "bin_centers_ev": bin_centers,
        "bin_probabilities": bin_probs,
        "single_bin_probabilities": single_bin_probs,
        "pileup_bin_probabilities": pileup_bin_probs,
        "pileup_fraction": f_pp,
    }


def expected_counts(
    config: SimulationConfig, live_time_years: float, mnu2_ev2: float | None = None
) -> tuple[np.ndarray, dict]:
    model = build_model(config, mnu2_ev2=mnu2_ev2)
    n_events = config.total_rate_hz * live_time_years * SECONDS_PER_YEAR
    return model["bin_probabilities"] * n_events, model


def expected_count_components(
    config: SimulationConfig, live_time_years: float, mnu2_ev2: float | None = None
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict]:
    model = build_model(config, mnu2_ev2=mnu2_ev2)
    n_events = config.total_rate_hz * live_time_years * SECONDS_PER_YEAR
    total = model["bin_probabilities"] * n_events
    single = model["single_bin_probabilities"] * n_events
    pileup = model["pileup_bin_probabilities"] * n_events
    return total, single, pileup, model

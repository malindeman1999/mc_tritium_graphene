from __future__ import annotations

import numpy as np


def make_endpoint_grid(endpoint_energy_ev: float, n_grid: int) -> np.ndarray:
    return np.linspace(0.0, 2.0 * endpoint_energy_ev + 50.0, n_grid)


def normalize_density(energy_ev: np.ndarray, density: np.ndarray) -> np.ndarray:
    density = np.clip(np.asarray(density, dtype=float), 0.0, None)
    area = np.trapezoid(density, energy_ev)
    if not np.isfinite(area) or area <= 0.0:
        raise ValueError("Cannot normalize a non-positive spectrum.")
    return density / area


def tritium_endpoint_spectrum(
    energy_ev: np.ndarray,
    endpoint_energy_ev: float,
    mnu2_ev2: float = 0.0,
) -> np.ndarray:
    """Normalized allowed beta spectrum over the full tritium energy range.

    Negative m_nu^2 is allowed for numerical derivatives, with the square-root
    term clipped only outside the physical endpoint support.
    """
    w = endpoint_energy_ev - energy_ev
    root_arg = np.maximum(w**2 - mnu2_ev2, 0.0)
    density = np.where((energy_ev >= 0.0) & (w > 0.0), w * np.sqrt(root_arg), 0.0)
    return normalize_density(energy_ev, density)


def blocking_acceptance(
    energy_ev: np.ndarray,
    blocking_voltage_ev: float,
    include_upward_hemisphere: bool = True,
) -> np.ndarray:
    """Fraction of all isotropic decays passing hemisphere and voltage cuts."""
    energy = np.asarray(energy_ev, dtype=float)
    acceptance = np.zeros_like(energy)
    valid = energy > max(blocking_voltage_ev, 0.0)
    cos_min = np.zeros_like(energy)
    cos_min[valid] = np.sqrt(np.clip(blocking_voltage_ev / energy[valid], 0.0, 1.0))
    acceptance[valid] = 1.0 - cos_min[valid]
    if include_upward_hemisphere:
        acceptance *= 0.5
    return acceptance

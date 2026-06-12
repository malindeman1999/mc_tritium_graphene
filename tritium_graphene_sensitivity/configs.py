from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path


SECONDS_PER_YEAR = 365.25 * 24 * 3600


@dataclass
class SimulationConfig:
    endpoint_energy_ev: float = 18_600.0
    mnu2_ev2: float = 0.100**2
    detector_fwhm_ev: float = 0.1
    zero_point_fwhm_ev: float = 0.5
    blocking_fraction: float = 0.51
    n_detectors: int = 100_000
    activity_bq: float = 178.0
    tau_eff_us: float = 0.0
    background_per_ev_year: float = 0.0
    live_time_years_target: float = 1.0
    chunk_days: float = 36.525
    n_grid: int = 65536
    n_bins: int = 50
    use_gpu: bool = False
    fit_low_offset_ev: float = -10.0
    fit_high_offset_ev: float = 0.1
    fit_method: str = "robust_mle"
    endpoint_weight: float = 10.0
    fit_use_flat_offset: bool = False
    parallel_fit_runs: int = 5
    rng_seed: int | None = 12345
    run_name: str = "tritium_graphene_run"
    output_dir: str = "runs"

    @property
    def q_ec_ev(self) -> float:
        return self.endpoint_energy_ev

    @property
    def energy_fwhm_ev(self) -> float:
        return (self.detector_fwhm_ev**2 + self.zero_point_fwhm_ev**2) ** 0.5

    @property
    def blocking_voltage_ev(self) -> float:
        return self.blocking_fraction * self.endpoint_energy_ev

    @property
    def tau_eff_s(self) -> float:
        return self.tau_eff_us * 1e-6

    @property
    def pileup_fraction(self) -> float:
        return self.activity_bq * self.tau_eff_s

    @property
    def total_rate_hz(self) -> float:
        return self.n_detectors * self.activity_bq

    @property
    def true_mnu_mev(self) -> float:
        return (max(self.mnu2_ev2, 0.0) ** 0.5) * 1000.0

    @property
    def output_path(self) -> Path:
        return Path(self.output_dir)

    def as_json_dict(self) -> dict:
        return asdict(self)


def config_from_dict(data: dict) -> SimulationConfig:
    data = dict(data)
    if "blocking_fraction" not in data and "blocking_voltage_ev" in data:
        endpoint = float(data.get("endpoint_energy_ev", data.get("q_ec_ev", 18_600.0)))
        data["blocking_fraction"] = float(data["blocking_voltage_ev"]) / endpoint if endpoint > 0.0 else 0.0
    known = {field.name for field in SimulationConfig.__dataclass_fields__.values()}
    return SimulationConfig(**{key: value for key, value in data.items() if key in known})

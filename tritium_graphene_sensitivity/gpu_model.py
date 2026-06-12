from __future__ import annotations

from .configs import SimulationConfig


def can_use_gpu() -> bool:
    return False


def build_model_gpu(config: SimulationConfig, mnu2_ev2: float | None = None) -> dict:
    _ = (config, mnu2_ev2)
    raise RuntimeError("GPU model is not implemented for the tritiated-graphene simulator.")

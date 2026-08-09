"""Week 1 ACL scaffold forward model.

This module validates a constant-parameter spring-mass-damper solver first,
then reuses the same solver for a time-varying scaffold-condition model.
"""

from dataclasses import dataclass
from typing import Union

import matplotlib.pyplot as plt
import numpy as np

ArrayLikeParameter = Union[float, np.ndarray]


@dataclass(frozen=True)
class SimulationConfig:
    """Configuration values for the forward simulation."""

    duration: float = 15.0
    dt: float = 0.001
    mass: float = 1.0
    x0: float = 0.0
    v0: float = 0.0
    scaffold_length: float = 0.05
    alpha: float = 0.3
    q0: float = 0.0
    k_min: float = 10.0
    k_max: float = 40.0
    c_min: float = 0.1
    c_max: float = 1.5


def create_time_array(config: SimulationConfig) -> np.ndarray:
    """Create a uniformly spaced time array that includes both endpoints."""

    if config.duration <= 0:
        raise ValueError("duration must be positive")
    if config.dt <= 0:
        raise ValueError("dt must be positive")

    step_count = int(round(config.duration / config.dt))
    return np.linspace(0.0, config.duration, step_count + 1)


def _as_parameter_array(
    value: ArrayLikeParameter,
    length: int,
    name: str,
) -> np.ndarray:
    """Convert a scalar or one-dimensional parameter into a full array."""

    if np.isscalar(value):
        array = np.full(length, float(value), dtype=float)
    else:
        array = np.asarray(value, dtype=float)
        if array.ndim != 1 or len(array) != length:
            raise ValueError(
                f"{name} must be a scalar or a one-dimensional array matching time"
            )

    if np.any(~np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    if np.any(array < 0):
        raise ValueError(f"{name} cannot contain negative values")

    return array


def simulate_spring_mass_damper(
    time: np.ndarray,
    force: np.ndarray,
    mass: float,
    stiffness: ArrayLikeParameter,
    damping: ArrayLikeParameter,
    x0: float = 0.0,
    v0: float = 0.0,
) -> np.ndarray:
    """Solve m*x'' + c*x' + k*x = F using central finite differences.

    ``stiffness`` and ``damping`` may each be either a single constant or an
    array with one value for every time sample.
    """

    time = np.asarray(time, dtype=float)
    force = np.asarray(force, dtype=float)

    if mass <= 0:
        raise ValueError("mass must be positive")
    if time.ndim != 1 or len(time) < 2:
        raise ValueError("time must contain at least two samples")
    if force.ndim != 1 or len(force) != len(time):
        raise ValueError("force must be one-dimensional and match time")
    if np.any(~np.isfinite(time)) or np.any(~np.isfinite(force)):
        raise ValueError("time and force must contain only finite values")

    time_steps = np.diff(time)
    if np.any(time_steps <= 0):
        raise ValueError("time values must be strictly increasing")
    if not np.allclose(time_steps, time_steps[0], rtol=1e-9, atol=1e-12):
        raise ValueError("time samples must be uniformly spaced")

    dt = float(time_steps[0])
    stiffness_array = _as_parameter_array(stiffness, len(time), "stiffness")
    damping_array = _as_parameter_array(damping, len(time), "damping")

    displacement = np.zeros_like(time)
    displacement[0] = x0

    # A central-difference recurrence needs x[0] and x[1]. This Taylor-based
    # starting expression uses the initial position, velocity, and force.
    displacement[1] = (
        (1.0 - stiffness_array[0] * dt**2 / (2.0 * mass)) * x0
        + (dt - damping_array[0] * dt**2 / (2.0 * mass)) * v0
        + dt**2 * force[0] / (2.0 * mass)
    )

    for index in range(1, len(time) - 1):
        denominator = mass / dt**2 + damping_array[index] / (2.0 * dt)
        current_weight = (
            2.0 * mass / dt**2 - stiffness_array[index]
        ) / denominator
        previous_weight = (
            damping_array[index] / (2.0 * dt) - mass / dt**2
        ) / denominator

        displacement[index + 1] = (
            current_weight * displacement[index]
            + previous_weight * displacement[index - 1]
            + force[index] / denominator
        )

    return displacement


def zero_force(time: np.ndarray) -> np.ndarray:
    """Return a force profile containing only zeros."""

    return np.zeros_like(np.asarray(time, dtype=float))


def constant_force(time: np.ndarray, magnitude: float) -> np.ndarray:
    """Return a force profile with the same magnitude at every time sample."""

    return np.full_like(np.asarray(time, dtype=float), magnitude, dtype=float)


def sinusoidal_force(
    time: np.ndarray,
    amplitude: float,
    omega: float,
    phase: float = 0.0,
) -> np.ndarray:
    """Return F(t) = amplitude * sin(omega*t + phase)."""

    time = np.asarray(time, dtype=float)
    return amplitude * np.sin(omega * time + phase)


def tensile_sinusoidal_force(
    time: np.ndarray,
    preload: float,
    amplitude: float,
    omega: float,
    phase: float = 0.0,
) -> np.ndarray:
    """Return a sinusoid with preload, clipped so it never becomes compressive."""

    raw_force = preload + sinusoidal_force(time, amplitude, omega, phase)
    return np.maximum(raw_force, 0.0)


def generate_condition_state(
    time: np.ndarray,
    q0: float,
    alpha: float,
) -> np.ndarray:
    """Advance dq/dt = alpha*(1-q) with a forward-Euler step."""

    time = np.asarray(time, dtype=float)
    if time.ndim != 1 or len(time) < 2:
        raise ValueError("time must contain at least two samples")
    if not 0.0 <= q0 <= 1.0:
        raise ValueError("q0 must be between 0 and 1")
    if alpha < 0:
        raise ValueError("alpha cannot be negative")

    condition = np.zeros_like(time)
    condition[0] = q0

    for index, dt in enumerate(np.diff(time)):
        if dt <= 0:
            raise ValueError("time values must be strictly increasing")
        condition[index + 1] = np.clip(
            condition[index] + dt * alpha * (1.0 - condition[index]),
            0.0,
            1.0,
        )

    return condition


def parameters_from_state(
    condition: np.ndarray,
    k_min: float,
    k_max: float,
    c_min: float,
    c_max: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Map q in [0, 1] linearly to stiffness and damping arrays."""

    condition = np.asarray(condition, dtype=float)
    if np.any(~np.isfinite(condition)):
        raise ValueError("condition must contain only finite values")
    if np.any((condition < 0.0) | (condition > 1.0)):
        raise ValueError("condition values must stay between 0 and 1")
    if k_min < 0 or k_max < k_min:
        raise ValueError("stiffness limits must satisfy 0 <= k_min <= k_max")
    if c_min < 0 or c_max < c_min:
        raise ValueError("damping limits must satisfy 0 <= c_min <= c_max")

    stiffness = k_min + (k_max - k_min) * condition
    damping = c_min + (c_max - c_min) * condition
    return stiffness, damping


def calculate_strain(
    displacement: np.ndarray,
    scaffold_length: float,
) -> np.ndarray:
    """Convert elongation/displacement into engineering strain x/L0."""

    if scaffold_length <= 0:
        raise ValueError("scaffold_length must be positive")
    return np.asarray(displacement, dtype=float) / scaffold_length


@dataclass(frozen=True)
class ValidationResult:
    """Outcome of one known-behavior validation check."""

    name: str
    passed: bool
    measured: float
    expected: float
    tolerance: float


def run_validation_checks() -> list[ValidationResult]:
    """Run known-physics checks before trusting the time-varying model."""

    results: list[ValidationResult] = []

    # Check 1: no force + no initial motion must remain exactly at zero.
    time = np.linspace(0.0, 2.0, 2001)
    zero_displacement = simulate_spring_mass_damper(
        time,
        zero_force(time),
        mass=1.0,
        stiffness=25.0,
        damping=0.8,
        x0=0.0,
        v0=0.0,
    )
    zero_error = float(np.max(np.abs(zero_displacement)))
    results.append(
        ValidationResult(
            name="Zero-input response",
            passed=zero_error <= 1e-12,
            measured=zero_error,
            expected=0.0,
            tolerance=1e-12,
        )
    )

    # Check 2: with constant force, the settled response should approach F/k.
    equilibrium_time = np.linspace(0.0, 20.0, 20001)
    equilibrium_displacement = simulate_spring_mass_damper(
        equilibrium_time,
        constant_force(equilibrium_time, 5.0),
        mass=1.0,
        stiffness=25.0,
        damping=5.0,
        x0=0.0,
        v0=0.0,
    )
    equilibrium_expected = 5.0 / 25.0
    equilibrium_measured = float(equilibrium_displacement[-1])
    results.append(
        ValidationResult(
            name="Constant-force equilibrium",
            passed=abs(equilibrium_measured - equilibrium_expected) <= 2e-3,
            measured=equilibrium_measured,
            expected=equilibrium_expected,
            tolerance=2e-3,
        )
    )

    # Check 3: a damped free response should lose most of its amplitude.
    decay_time = np.linspace(0.0, 10.0, 10001)
    decay_displacement = simulate_spring_mass_damper(
        decay_time,
        zero_force(decay_time),
        mass=1.0,
        stiffness=25.0,
        damping=1.5,
        x0=0.01,
        v0=0.0,
    )
    early_peak = float(np.max(np.abs(decay_displacement[:2000])))
    late_peak = float(np.max(np.abs(decay_displacement[-2000:])))
    amplitude_ratio = late_peak / early_peak
    results.append(
        ValidationResult(
            name="Damped free response",
            passed=amplitude_ratio < 0.1,
            measured=amplitude_ratio,
            expected=0.0,
            tolerance=0.1,
        )
    )

    # Check 4: halving dt should produce a very similar solution.
    coarse_time = np.linspace(0.0, 5.0, 2501)
    fine_time = np.linspace(0.0, 5.0, 5001)
    coarse = simulate_spring_mass_damper(
        coarse_time,
        sinusoidal_force(coarse_time, 2.0, 1.2),
        mass=1.0,
        stiffness=25.0,
        damping=0.8,
    )
    fine = simulate_spring_mass_damper(
        fine_time,
        sinusoidal_force(fine_time, 2.0, 1.2),
        mass=1.0,
        stiffness=25.0,
        damping=0.8,
    )
    fine_at_coarse_points = fine[::2]
    refinement_error = float(np.max(np.abs(coarse - fine_at_coarse_points)))
    results.append(
        ValidationResult(
            name="Time-step refinement",
            passed=refinement_error <= 2e-4,
            measured=refinement_error,
            expected=0.0,
            tolerance=2e-4,
        )
    )

    return results


def run_time_varying_demo(config: SimulationConfig) -> dict[str, np.ndarray]:
    """Run the full Week 1 time-varying scaffold-condition demonstration."""

    if config.scaffold_length <= 0:
        raise ValueError("scaffold_length must be positive")

    time = create_time_array(config)

    # The preload keeps the simulated scaffold in tension rather than allowing
    # the sine wave to become a compressive load.
    force = tensile_sinusoidal_force(
        time,
        preload=5.0,
        amplitude=5.0,
        omega=3.14,
    )

    condition = generate_condition_state(time, config.q0, config.alpha)
    stiffness, damping = parameters_from_state(
        condition,
        config.k_min,
        config.k_max,
        config.c_min,
        config.c_max,
    )

    displacement = simulate_spring_mass_damper(
        time=time,
        force=force,
        mass=config.mass,
        stiffness=stiffness,
        damping=damping,
        x0=config.x0,
        v0=config.v0,
    )
    strain = calculate_strain(displacement, config.scaffold_length)

    return {
        "time": time,
        "force": force,
        "condition": condition,
        "stiffness": stiffness,
        "damping": damping,
        "displacement": displacement,
        "strain": strain,
    }


def plot_demo_results(result: dict[str, np.ndarray]) -> None:
    """Plot force, displacement, strain, q, stiffness, and damping."""

    time = result["time"]
    figure, axes = plt.subplots(4, 1, figsize=(11, 11), sharex=True)

    displacement_axis = axes[0]
    displacement_axis.plot(
        time,
        result["displacement"],
        label="Displacement x(t)",
    )
    force_axis = displacement_axis.twinx()
    force_axis.plot(
        time,
        result["force"],
        linestyle=":",
        alpha=0.5,
        label="Force F(t)",
    )
    displacement_axis.set_ylabel("Displacement (m)")
    force_axis.set_ylabel("Force (N)")
    displacement_axis.set_title("ACL Scaffold Week 1 Forward Model")
    displacement_axis.grid(True)

    axes[1].plot(time, result["strain"])
    axes[1].set_ylabel("Engineering strain")
    axes[1].grid(True)

    axes[2].plot(time, result["condition"])
    axes[2].set_ylabel("Condition q(t)")
    axes[2].set_ylim(-0.05, 1.05)
    axes[2].grid(True)

    parameter_axis = axes[3]
    parameter_axis.plot(
        time,
        result["stiffness"],
        label="Stiffness k(t)",
    )
    damping_axis = parameter_axis.twinx()
    damping_axis.plot(
        time,
        result["damping"],
        linestyle="--",
        label="Damping c(t)",
    )
    parameter_axis.set_xlabel("Time (s)")
    parameter_axis.set_ylabel("Stiffness (N/m)")
    damping_axis.set_ylabel("Damping (N·s/m)")
    parameter_axis.grid(True)

    figure.tight_layout()
    plt.show()


def print_validation_report(results: list[ValidationResult]) -> None:
    """Print a compact pass/fail table for the validation checks."""

    print("Week 1 validation checks")
    print("-" * 88)
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(
            f"{status:4s} | {result.name:28s} | "
            f"measured={result.measured:.6g}, "
            f"expected={result.expected:.6g}, "
            f"tolerance={result.tolerance:.2g}"
        )


def main() -> None:
    """Run validation first, then run and plot the time-varying model."""

    validation_results = run_validation_checks()
    print_validation_report(validation_results)

    if not all(result.passed for result in validation_results):
        raise RuntimeError(
            "One or more validation checks failed; the demonstration was not run."
        )

    demo = run_time_varying_demo(SimulationConfig())
    print("\nTime-varying scaffold demonstration")
    print(f"Final q: {demo['condition'][-1]:.4f}")
    print(f"Final stiffness: {demo['stiffness'][-1]:.3f} N/m")
    print(f"Final damping: {demo['damping'][-1]:.3f} N·s/m")
    print(f"Peak displacement: {np.max(np.abs(demo['displacement'])):.6f} m")
    print(f"Peak strain: {np.max(np.abs(demo['strain'])):.3%}")

    plot_demo_results(demo)


if __name__ == "__main__":
    main()

import numpy as np
from scipy import constants


def of_ratio_to_mass_fraction(of_ratio: float) -> tuple[float, float]:
    """
    Converts an oxidizer to fuel ratio to a mass fraction of oxidizer and fuel.

    Args:
        of_ratio (float): The oxidizer to fuel ratio.

    Returns:
        tuple[float, float]: The mass fraction of oxidizer and fuel.
    """
    return of_ratio / (of_ratio + 1), 1 / (of_ratio + 1)


def mass_fraction_to_of_ratio(
    mass_fraction_oxidizer: float, mass_fraction_fuel: float
) -> float:
    """
    Converts a mass fraction of oxidizer and fuel to an oxidizer to fuel ratio.

    Args:
        mass_fraction_oxidizer (float): The mass fraction of oxidizer.
        mass_fraction_fuel (float): The mass fraction of fuel.

    Returns:
        float: The oxidizer to fuel ratio.
    """
    return mass_fraction_oxidizer / mass_fraction_fuel


def total_flow(thrust: float, i_sp: float) -> float:
    """
    Calculates the total flow rate, given the desired thrust and specific
    impulse.

    Args:
        thrust (float): The thrust.
        i_sp (float): The specific impulse.

    Returns:
        float: The total flow rate.
    """
    return thrust / (i_sp * constants.g)


def fuel_flow_from_of_ratio(
    of_ratio: float,
    total_flow: float,
) -> float:
    """
    Calculates the fuel flow rate from an oxidizer to fuel ratio.

    Args:
        of_ratio (float): The oxidizer to fuel ratio.
        total_flow (float): The total flow rate.

    Returns:
        float: The fuel flow rate.
    """
    return total_flow * (1 / (of_ratio + 1))


def oxidizer_flow_from_of_ratio(
    of_ratio: float,
    total_flow: float,
) -> float:
    """
    Calculates the oxidizer flow rate from an oxidizer to fuel ratio.

    Args:
        of_ratio (float): The oxidizer to fuel ratio.
        total_flow (float): The total flow rate.

    Returns:
        float: The oxidizer flow rate.
    """
    return total_flow * (of_ratio / (of_ratio + 1))


def throat_area_from_mass_flow(
    mass_flow: float,
    pressure: float,
    temperature: float,
    gamma: float,
    molar_mass: float,
) -> float:
    """
    Calculates the throat area from the mass flow rate, pressure, temperature,
    and ratio of specific heats.

    Args:
        mass_flow (float): The mass flow rate - constant throughout the nozzle.
        pressure (float): The pressure at the throat.
        temperature (float): The temperature at the throat.
        gamma (float): The ratio of specific heats.
        molar_mass (float): The molar mass of the propellant.

    Returns:
        float: The throat area.
    """
    return (
        mass_flow / pressure * np.sqrt(constants.R * temperature / gamma / molar_mass)
    )


def fuel_spray_injector_area(
    flow: float,
    orifice_discharge_coefficient: float,
    density: float,
    pressure_drop: float,
) -> float:
    """
    Calculates the fuel spray injector area from the mass flow rate, pressure, temperature,
    and ratio of specific heats.

    Args:
        flow (float): The mass flow rate - constant throughout the nozzle.
        orifice_discharge_coefficient (float): The pressure at the throat.
        density (float): The temperature at the throat.
        pressure_drop (float): The ratio of specific heats.

    Returns:
        float: The throat area.
    """
    return flow / (orifice_discharge_coefficient * np.sqrt(2 * density * pressure_drop))

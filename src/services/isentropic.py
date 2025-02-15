

def temperature_at_throat(chamber_temperature: float, gamma: float) -> float:
    """Returns the temperature at the nozzle throat.

    Args:
        chamber_temperature (float): The temperature of the combustion chamber.
        gamma (float): The ratio of specific heats of the combustion gas.

    Returns:
        float: The temperature at the nozzle throat.
    """
    return chamber_temperature * (2 / (gamma + 1))


def pressure_at_throat(chamber_pressure: float, gamma: float) -> float:
    """Returns the pressure at the nozzle throat.

    Args:
        chamber_pressure (float): The pressure of the combustion chamber.
        gamma (float): The ratio of specific heats of the combustion gas.

    Returns:
        float: The pressure at the nozzle throat.
    """
    return chamber_pressure * (2 / (gamma + 1)) ** (gamma / (gamma - 1))


def optimal_expansion_ratio(
    chamber_pressure: float, atmospheric_pressure: float, gamma: float
) -> float:
    """
    Calculates the optimal expansion ratio given the chamber pressure,
    atmospheric pressure, and specific heat ratio.

    Args:
        chamber_pressure (float): The pressure in the combustion chamber
            (in Pascals).
        atmospheric_pressure (float): The atmospheric pressure (in Pascals).
        gamma (float): The specific heat ratio.

    Returns:
        float: The optimal expansion ratio.

    """
    pressure_ratio = atmospheric_pressure / chamber_pressure
    optimal_expansion_ratio = (
        ((gamma + 1) / 2) ** (1 / (gamma - 1))
        * pressure_ratio ** (1 / gamma)
        * ((gamma + 1) / (gamma - 1) * (1 - pressure_ratio ** ((gamma - 1) / gamma)))
        ** 0.5
    ) ** -1
    return optimal_expansion_ratio

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

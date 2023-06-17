import math


def area_to_diameter(area: float) -> float:
    """
    Calculates the diameter of a circle from its area.

    Args:
        area (float): The area of the circle.

    Returns:
        float: The diameter of the circle.
    """
    return 2 * math.sqrt(area / math.pi)


def diameter_to_area(diameter: float) -> float:
    """
    Calculates the area of a circle from its diameter.

    Args:
        diameter (float): The diameter of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * (diameter / 2) ** 2

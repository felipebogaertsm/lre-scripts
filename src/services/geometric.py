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

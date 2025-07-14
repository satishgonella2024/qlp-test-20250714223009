import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    Formula: area = π * radius^2

    Parameters:
    radius (float): The radius of the circle

    Returns:
    float: The area of the circle
    """
    return math.pi * radius**2

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Formula: area = length * width

    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle

    Returns:
    float: The area of the rectangle
    """
    return length * width

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Formula: area = 0.5 * base * height

    Parameters:
    base (float): The base of the triangle
    height (float): The height of the triangle

    Returns:
    float: The area of the triangle
    """
    return 0.5 * base * height

# Example usage
circle_area = calculate_circle_area(5)
rectangle_area = calculate_rectangle_area(4, 6)
triangle_area = calculate_triangle_area(3, 8)

print("Circle Area:", circle_area)
print("Rectangle Area:", rectangle_area)
print("Triangle Area:", triangle_area)

import math

class ShapeError(Exception):
    """Custom exception for shape errors."""
    pass


def calculate_area(shape: str, **dimensions) -> float:
    """
    Calculate the area of a given shape.

    Supported shapes and required dimensions:
    - circle: radius (float > 0)
    - rectangle: length (float > 0), width (float > 0)
    - triangle: base (float > 0), height (float > 0)

    Args:
        shape (str): The type of shape ('circle', 'rectangle', 'triangle').
        **dimensions: Arbitrary keyword arguments for shape dimensions.

    Returns:
        float: The calculated area.

    Raises:
        ShapeError: If shape is unsupported or required dimensions are missing/invalid.
        TypeError: If dimension values are not numbers.
    """
    shape = shape.strip().lower()

    def validate_positive_number(value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Dimension '{name}' must be a number (int or float).")
        if value <= 0:
            raise ShapeError(f"Dimension '{name}' must be greater than zero.")

    if shape == 'circle':
        radius = dimensions.get('radius')
        if radius is None:
            raise ShapeError("Missing required dimension 'radius' for circle.")
        validate_positive_number(radius, 'radius')
        return math.pi * radius ** 2

    elif shape == 'rectangle':
        length = dimensions.get('length')
        width = dimensions.get('width')
        if length is None or width is None:
            raise ShapeError("Missing required dimensions 'length' and/or 'width' for rectangle.")
        validate_positive_number(length, 'length')
        validate_positive_number(width, 'width')
        return length * width

    elif shape == 'triangle':
        base = dimensions.get('base')
        height = dimensions.get('height')
        if base is None or height is None:
            raise ShapeError("Missing required dimensions 'base' and/or 'height' for triangle.")
        validate_positive_number(base, 'base')
        validate_positive_number(height, 'height')
        return 0.5 * base * height

    else:
        raise ShapeError(f"Unsupported shape '{shape}'. Supported shapes: circle, rectangle, triangle.")


if __name__ == '__main__':
    # Example usage
    try:
        print(f"Circle area (r=3): {calculate_area('circle', radius=3):.2f}")
        print(f"Rectangle area (l=4, w=5): {calculate_area('rectangle', length=4, width=5):.2f}")
        print(f"Triangle area (b=6, h=7): {calculate_area('triangle', base=6, height=7):.2f}")
    except (ShapeError, TypeError) as e:
        print(f"Error: {e}")
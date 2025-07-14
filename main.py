def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Base and height must be numerical values")
    if base < 0 or height < 0:
        return -0.5 * base * height
    return 0.5 * base * height
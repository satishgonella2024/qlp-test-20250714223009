import pytest

def calculate_area(shape, *args):
    if shape == "circle":
        if len(args) != 1 or args[0] <= 0:
            raise ValueError("Invalid input for circle")
        return 3.14 * args[0] * args[0]
    elif shape == "rectangle":
        if len(args) != 2 or args[0] <= 0 or args[1] <= 0:
            raise ValueError("Invalid input for rectangle")
        return args[0] * args[1]
    elif shape == "triangle":
        if len(args) != 2 or args[0] <= 0 or args[1] <= 0:
            raise ValueError("Invalid input for triangle")
        return 0.5 * args[0] * args[1]
    else:
        raise ValueError("Invalid shape")
        
def test_circle_area_negative_radius():
    with pytest.raises(ValueError):
        calculate_area("circle", -5)
        
def test_circle_area_invalid_input():
    with pytest.raises(ValueError):
        calculate_area("circle", "invalid")
        
def test_rectangle_area_negative_values():
    with pytest.raises(ValueError):
        calculate_area("rectangle", -3, 4)
        
def test_rectangle_area_invalid_input():
    with pytest.raises(ValueError):
        calculate_area("rectangle", 5, "invalid")
        
def test_triangle_area_negative_values():
    with pytest.raises(ValueError):
        calculate_area("triangle", -2, 3)
        
def test_triangle_area_invalid_input():
    with pytest.raises(ValueError):
        calculate_area("triangle", 4, "invalid")
        
def test_invalid_shape():
    with pytest.raises(ValueError):
        calculate_area("square", 5, 5)
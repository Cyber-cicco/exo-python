def get_square_area(side):
    return side ** 2
def get_rectangle_area(length, width):
    return length * width
def get_circle_area(radius):
    return 3.14 * radius ** 2
if __name__ == "__main__":
    square1_side = 5
    square1_area = get_square_area(side=square1_side)
    print(f"Square 1: side={square1_side}, area={square1_area}")
    square2_side = 4
    square2_area = get_square_area(side=square2_side)
    print(f"Square 2: side={square2_side}, area={square2_area}")
    rectangle_length = 5
    rectangle_width = 3
    rectangle_area = get_rectangle_area(length=rectangle_length, width=rectangle_width)
    print(f"Rectangle: length={rectangle_length}, width={rectangle_width}, are={rectangle_area}")
    circle1_area = get_circle_area(radius=circle1_radius)
    print(f"Circle 1: radius={circle1_radius}, area={circle1_area}")
    circle2_radius = 3
    circle2_area = get_circle_area(radius=circle2_radius)
    print(f"Circle 2: radius={circle2_radius}, area={circle2_area}")
    circle1_radius = 2

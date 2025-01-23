from typing import Callable

class Shape:

    PI = 3.14159

    def __init__(self):
        pass

    def get_area(self) -> float:
        return 0


class Rectangle(Shape):

    def __init__(self, width:float, length:float):
        super().__init__()
        self.width = width
        self.length = length

    def get_area(self) -> float:
        return self.width * self.length


class Square(Rectangle):

    def __init__(self, side_length:float):
        super().__init__(side_length, side_length)
        self.side_length = side_length


class Circle(Shape):

    def __init__(self, radius:float):
        super().__init__()
        self.radius = radius

    def get_area(self) -> float:
        return self.radius * self.radius * Shape.PI

if __name__ == "__main__":
    square_1 = Square(5)
    print(f"Square 1: side={square_1.side_length}, area={square_1.get_area()}")
    square_2 = Square(4)
    print(f"Square 2: side={square_2.side_length}, area={square_2.get_area()}")
    rectangle = Rectangle(5, 3)
    print(f"Rectangle: length={rectangle.length}, width={rectangle.width}, area={rectangle.get_area()}")
    circle_1 = Circle(2)
    print(f"Circle 1: radius={circle_1.radius}, area={circle_1.get_area()}")
    circle_2 = Circle(3)
    print(f"Circle 2: radius={circle_2.radius}, area={circle_2.get_area()}")


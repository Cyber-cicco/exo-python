from typing import Callable

class Shape:

    PI = 3.14159

    def __init__(self):
        pass

    def get_area(self) -> float:
        return 0



class Circle(Shape):

    def __init__(self, radius:float):
        super().__init__()
        self.radius = radius

    def get_area(self) -> float:
        return self.radius * self.radius * Shape.PI

class Cylinder(Circle):

    def __init__(self, radius:float, height:float):
        super().__init__(radius)
        self.height = height

    def get_volume(self) -> float:
        return self.get_area() * self.height

    def __str__(self) -> str:
        return f"Cylindre de rayon {self.radius} et hauteur {self.height}"

if __name__ == "__main__":
    cylinder = Cylinder(3, 5)
    print(cylinder)
    print(f"Volume du cylindre : {cylinder.get_volume()} cm3")

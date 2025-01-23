class Complex:

    def __init__(self, reel:float, complex:float) -> None:
        self.complex = complex
        self.reel = reel

    def __add__(self, o):
        return self.complex + o.complex, self.reel + o.reel

    def __str__(self) -> str:
        return f"{self.complex}i + {self.reel}"

if __name__ == "__main__":
    num_1 = Complex(3, 3)
    num_2 = Complex(6, 6)
    print(num_2 + num_1)

class Color:
    def __init__(self, r : int, g : int, b : int, a : int = 255) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def tuple(self) -> tuple[int, int, int, int]:
        return (self.r, self.g, self.b, self.a)

White = Color(255, 255, 255, 255)
Black = Color(0, 0, 0, 255)
Red = Color(255, 0, 0, 255)
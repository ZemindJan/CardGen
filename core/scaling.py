from core.geometry import Point

class Scaling:
    def __init__(self, multiplier : float, offset : float) -> None:
        self.multiplier = multiplier
        self.offset = offset

    def __add__(self, other):
        return Scaling(self.multiplier, self.offset + other)
    
    def __mul__(self, other):
        return Scaling(self.multiplier * other, self.offset * other)
    
    def __sub__(self, other):
        return Scaling(self.multiplier, self.offset - other)
    
    def __truediv__(self, other):
        return Scaling(self.multiplier / other, self.offset / 2)
    
def scale(value, source):
    if isinstance(value, int):
        return value
    elif isinstance(value, Scaling):
        return source * value.multiplier + value.offset
    elif isinstance(value, Point) and isinstance(source, Point):
        return Point(scale(value.x, source.x), scale(value.y, source.y))
    else:
        1 / 0

PARENT = Scaling(1.0, 0)
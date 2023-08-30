class Point():
    def __init__(self, x : float, y : float) -> None:
        self.x = x 
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)
    
    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def to(self, p2) -> 'Rect':
        return Rect(self, p2)
    
    def tuple(self):
        return (self.x, self.y)
    
    def int_tuple(self):
        return (int(self.x), int(self.y))
    
    @classmethod
    def x_span(cls, value):
        return Point(value, 0)
    
    @classmethod
    def y_span(cls, value):
        return Point(0, value)
    
    @classmethod
    def zero(cls):
        return Point(0, 0)

class Rect():
    def __init__(self, p1 : Point, p2 : Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def size(self) -> Point:
        return self.p2 - self.p1
    
    def __add__(self, point):
        return Rect(self.p1 + point, self.p2 + point)
    
    def center(self) -> Point:
        return (self.p1 + self.p2) / 2
    
    def int_tuple(self):
        return int(self.p1.x), int(self.p1.y), int(self.p2.x), int(self.p2.y)
    
    def round(self):
        self.p1 = Point(*self.p1.int_tuple())
        self.p2 = Point(*self.p2.int_tuple())

    @classmethod
    def from_size(self, p1 : Point, size : Point) -> 'Rect':
        return Rect(p1, p1 + size)
    
    def __contains__(self, other):
        if isinstance(other, Point):
            return self.p1.x <= other.x <= self.p2.x and self.p1.y <= other.y <= self.p2.y
        elif isinstance(other, Rect):
            return other.p1 in self and other.p2 in self
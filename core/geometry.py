Value = float | int

class Point():
    x : Value
    y : Value

    def __init__(self, x : Value, y : Value) -> None:
        self.x = x 
        self.y = y

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])
    
    def __eq__(self, other : 'Point'):
        return self.x == other.x and self.y == other.y
    
    def __radd__(self, other):
        return self + other
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __sub__(self, other):
        return Point(self.x - other[0], self.y - other[1])
    
    def __rsub__(self, other):
        return -(self - other)

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
    
    @staticmethod
    def x_span(value):
        return Point(value, 0)
    
    @staticmethod
    def y_span(value):
        return Point(0, value)
    
    @staticmethod
    def zero():
        return Point(0, 0)
    
    def __len__(self) -> int:
        return 4
    
    def __getitem__(self, index):
        return [self.x, self.y][index]
    
    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'

class Rect():
    p1 : Point
    p2 : Point

    def __init__(self, p1 : Point, p2 : Point) -> None:
        self.p1 = p1
        self.p2 = p2

    @staticmethod
    def from_tuple(tuple : tuple[Value, Value, Value, Value]) -> 'Rect':
        return Rect(Point(tuple[0], tuple[1]), Point(tuple[2], tuple[3]))

    def size(self) -> Point:
        return self.p2 - self.p1
    
    def __add__(self, point):
        return Rect(self.p1 + point, self.p2 + point)
    
    def center(self) -> Point:
        return (self.p1 + self.p2) / 2
    
    def int_tuple(self) -> tuple[int, int, int, int]:
        return tuple(map(int, self))
    
    def rounded(self) -> 'Rect':
        return Rect.from_tuple(tuple(map(int, self)))

    def __len__(self) -> int:
        return 4
    
    def __getitem__(self, index):
        return [self.p1.x, self.p1.y, self.p2.x, self.p2.y][index]

    @classmethod
    def from_size(self, p1 : Point, size : Point) -> 'Rect':
        return Rect(p1, p1 + size)
    
    def __contains__(self, other):
        if len(other) == 2:
            return self.p1.x <= other[0] <= self.p2.x and self.p1.y <= other[1] <= self.p2.y
        elif len(other) == 4:
            return (other[0], other[1]) in self and (other[2], other[3]) in self
    
    def __repr__(self) -> str:
        return f'Rect[{self.p1} to {self.p2}]'
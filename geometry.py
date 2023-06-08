class Vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(
            self.x + other.x,
            self.y + other.y,
        )
    
    def __radd__(self, other):
        return Vec2(
            self.x + other.x,
            self.y + other.y,
        )
    
    def __sub__(self, other):
        return Vec2(
            self.x - other.x,
            self.y - other.y,
        )
    
    def __rsub__(self, other):
        return Vec2(
            other.x - self.x,
            other.y - self.y,
        )
    
    def __mul__(self, other):
        return Vec2(
            self.x * other,
            self.y * other,
        )
    
    def __rmul__(self, other):
        return Vec2(
            self.x * other,
            self.y * other,
        )

    def __div__(self, other):
        return Vec2(
            self.x / other,
            self.y / other
        )
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        
        if index == 1:
            return self.y
    
    def tuple(self):
        return self.x, self.y
    
    def to_ints(self):
        return Vec2(
            int(self.x),
            int(self.y)
        )
    
class Rect:
    def __init__(self, p1 : Vec2, p2 : Vec2) -> None:   
        self.p1 = p1
        self.p2 = p2

    def size(self) -> Vec2:
        return self.p2 - self.p1
    
    def to_tuple(self) -> tuple[int, int, int, int]:
        return (self.p1[0], self.p1[1], self.p2[0], self.p2[1])
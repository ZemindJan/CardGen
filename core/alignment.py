from enum import Enum
from core.geometry import Point, Rect

class YAlignment(Enum):
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2

class XAlignment(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2

class _Alignment:
    x : XAlignment
    y : YAlignment

    def __init__(self, y_align : int, x_align : int) -> None:
        self.x = x_align
        self.y = y_align

    def get_root(self, rect : Rect) -> Point:
        x = rect.p1.x
        y = rect.p1.y

        if self.x == XAlignment.CENTER:
            x = (rect.p1.x + rect.p2.x) / 2
        elif self.x == XAlignment.RIGHT:
            x = rect.p2.x

        if self.y == YAlignment.MIDDLE:
            y = (rect.p1.y + rect.p2.y) / 2
        elif self.y == YAlignment.BOTTOM:
            y = rect.p2.y

        return Point(x, y)

class Alignment(Enum):
    x : XAlignment
    y : YAlignment

    TOP_LEFT      : 'Alignment' = _Alignment(YAlignment.TOP, XAlignment.LEFT)
    TOP_CENTER    : 'Alignment' = _Alignment(YAlignment.TOP, XAlignment.CENTER)
    TOP_RIGHT     : 'Alignment' = _Alignment(YAlignment.TOP, XAlignment.RIGHT)
    MIDDLE_LEFT   : 'Alignment' = _Alignment(YAlignment.MIDDLE, XAlignment.LEFT)
    MIDDLE_CENTER : 'Alignment' = _Alignment(YAlignment.MIDDLE, XAlignment.CENTER)
    MIDDLE_RIGHT  : 'Alignment' = _Alignment(YAlignment.MIDDLE, XAlignment.RIGHT)
    BOTTOM_LEFT   : 'Alignment' = _Alignment(YAlignment.BOTTOM, XAlignment.LEFT)
    BOTTOM_CENTER : 'Alignment' = _Alignment(YAlignment.BOTTOM, XAlignment.CENTER)
    BOTTOM_RIGHT  : 'Alignment' = _Alignment(YAlignment.BOTTOM, XAlignment.RIGHT)

    def get_root(self, rect : Rect) -> Point:
        return _Alignment.get_root(self.value, rect)
    
    def get_x(self):
        return self.value.x
    
    def get_y(self):
        return self.value.y

    x = property(fget=get_x)
    y = property(fget=get_y)

    
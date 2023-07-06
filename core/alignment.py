from core.geometry import Point, Rect

_Top = 0
_Middle = 1
_Bottom = 2

_Left = 0
_Center = 1
_Right = 2

class Alignment:
    def __init__(self, x_align : int, y_align : int) -> None:
        self.x_align = x_align
        self.y_align = y_align

    def get_root(self, rect : Rect) -> Point:
        x = rect.p1.x
        y = rect.p1.y

        if self.x_align == _Center:
            x = (rect.p1.x + rect.p2.x) / 2
        elif self.x_align == _Right:
            x = rect.p2.x

        if self.y_align == _Middle:
            y = (rect.p1.y + rect.p2.y) / 2
        elif self.y_align == _Bottom:
            y = rect.p2.y

        return Point(x, y)

TopLeft = Alignment(_Top, _Left)
TopCenter = Alignment(_Top, _Center)
TopRight = Alignment(_Top, _Right)
MiddleLeft = Alignment(_Middle, _Left)
MiddleCenter = Alignment(_Middle, _Center)
MiddleRight = Alignment(_Middle, _Right)
BottomLeft = Alignment(_Bottom, _Left)
BottomCenter = Alignment(_Bottom, _Center)
BottomRight = Alignment(_Bottom, _Right)
from core.geometry import Point, Rect

Top = 0
Middle = 1
Bottom = 2

Left = 0
Centered = 1
Right = 2

class Alignment:
    def __init__(self, x_align : int, y_align : int) -> None:
        self.x_align = x_align
        self.y_align = y_align

    def get_root(self, rect : Rect) -> Point:
        x = rect.p1.x
        y = rect.p1.y

        if self.x_align == Centered:
            x = (rect.p1.x + rect.p2.x) / 2
        elif self.x_align == Right:
            x = rect.p2.x

        if self.y_align == Middle:
            y = (rect.p1.y + rect.p2.y) / 2
        elif self.y_align == Bottom:
            y = rect.p2.y

        return Point(x, y)

TopLeft = Alignment(Top, Left)
TopCenter = Alignment(Top, Centered)
TopRight = Alignment(Top, Right)
MiddleLeft = Alignment(Middle, Left)
MiddleCenter = Alignment(Middle, Centered)
MiddleRight = Alignment(Middle, Right)
BottomLeft = Alignment(Bottom, Left)
BottomCenter = Alignment(Bottom, Centered)
BottomRight = Alignment(Bottom, Right)
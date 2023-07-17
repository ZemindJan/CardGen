from core.geometry import Point, Rect

top_y_align = 0
middle_y_align = 1
bottom_y_align = 2

left_x_align = 0
center_x_align = 1
right_x_align = 2

class Alignment:
    def __init__(self, y_align : int, x_align : int) -> None:
        self.x_align = x_align
        self.y_align = y_align

    def get_root(self, rect : Rect) -> Point:
        x = rect.p1.x
        y = rect.p1.y

        if self.x_align == center_x_align:
            x = (rect.p1.x + rect.p2.x) / 2
        elif self.x_align == right_x_align:
            x = rect.p2.x

        if self.y_align == middle_y_align:
            y = (rect.p1.y + rect.p2.y) / 2
        elif self.y_align == bottom_y_align:
            y = rect.p2.y

        return Point(x, y)

TopLeft = Alignment(top_y_align, left_x_align)
TopCenter = Alignment(top_y_align, center_x_align)
TopRight = Alignment(top_y_align, right_x_align)
MiddleLeft = Alignment(middle_y_align, left_x_align)
MiddleCenter = Alignment(middle_y_align, center_x_align)
MiddleRight = Alignment(middle_y_align, right_x_align)
BottomLeft = Alignment(bottom_y_align, left_x_align)
BottomCenter = Alignment(bottom_y_align, center_x_align)
BottomRight = Alignment(bottom_y_align, right_x_align)
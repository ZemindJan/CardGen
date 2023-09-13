from PIL import Image
from core.alignment import Alignment
from elements.element import CardElement
from core.geometry import Point, Rect
from core.color import RGBA, Color
from core.schema import Schema
from PIL import ImageDraw
from elements.shape import ShapeElement, Outline

def find_size(points : list[Point]) -> Point:
    xs = [point.x for point in points]
    ys = [point.y for point in points]

    return Point(max(xs) - min(xs), max(ys) - min(ys))

class PolygonElement(ShapeElement):
    def __init__(self, 
                 points : list[Point], 
                 fill: Color = None, 
                 offset: Point = None, 
                 stretch: bool = True, 
                 alignment: Alignment = None, 
                 outline: Outline | None = None, 
                 children : list[CardElement] = None, 
                 visible : bool = True) -> None:
        super().__init__(size=find_size(points), fill=fill, offset=offset, alignment=alignment, outline=outline, children=children, visible=visible)
        self.points = points
        self.stretch = stretch

    def calculate_area(self, parent_area: Rect) -> Rect:
        if self.stretch:
            return parent_area

        return super().calculate_area(parent_area)

    def draw_shape(self, draw: ImageDraw.ImageDraw, area: Rect, fill: RGBA, outline: RGBA = None, outlineWidth: int = 0):
        x_ratio = area.size().x / self.size.x
        y_ratio = area.size().y / self.size.y

        if not self.stretch:
            x_ratio = 1
            y_ratio = 1

        points = [area.p1 + Point(point.x * x_ratio, point.y * y_ratio) for point in self.points]
        xy = [point.int_tuple() for point in points]

        draw.polygon(xy=xy, fill=fill.tuple(), outline=outline.tuple() if outline else None, width=outlineWidth)
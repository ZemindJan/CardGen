from PIL import Image
from core.alignment import Alignment
from elements.element import CardElement
from core.geometry import Point, Rect
from core.color import Color
from core.schema import Schema
from PIL import ImageDraw
from elements.shape import ShapeElement

def find_size(points : list[Point]) -> Point:
    xs = [point.x for point in points]
    ys = [point.y for point in points]

    return Point(max(xs) - min(xs), max(ys) - min(ys))

class PolygonElement(ShapeElement):
    def __init__(self, fill: Color, offset: Point, points : list[Point], stretch: bool = True, alignment: Alignment = None, outline: Color = None, outlineWidth: int = 0, children : list[CardElement] = None) -> None:
        super().__init__(fill, offset, find_size(points), alignment, outline, outlineWidth, children)
        self.points = points
        self.stretch = stretch

    def calculate_size(self, parent_area: Rect) -> Rect:
        if self.stretch:
            return parent_area

        return super().calculate_size(parent_area)

    def draw_shape(self, draw: ImageDraw.ImageDraw, area: Rect, fill: Color, outline: Color = None, outlineWidth: int = 0):
        x_ratio = area.size().x / self.size.x
        y_ratio = area.size().y / self.size.y

        if not self.stretch:
            x_ratio = 1
            y_ratio = 1

        points = [area.p1 + Point(point.x * x_ratio, point.y * y_ratio) for point in self.points]
        xy = [point.int_tuple() for point in points]

        draw.polygon(xy=xy, fill=fill.tuple(), outline=outline.tuple() if outline else None, width=outlineWidth)
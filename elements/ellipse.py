from PIL import Image
from core.alignment import Alignment
from elements.element import CardElement
from core.geometry import Point, Rect
from core.color import Color
from core.schema import Schema
from PIL import ImageDraw
from elements.shape import ShapeElement

class EllipseElement(ShapeElement):
    def __init__(self, fill: Color, offset: Point, size: Point, alignment: Alignment = None, outline: Color = None, outlineWidth: int = 0, children : list[CardElement] = None) -> None:
        super().__init__(fill, offset, size, alignment, outline, outlineWidth, children)

    def draw_shape(self, draw: ImageDraw.ImageDraw, area: Rect, fill: Color, outline: Color = None, outlineWidth: int = 0):
        draw.ellipse(xy=area.int_tuple(), fill=fill.tuple(), outline=outline.tuple() if outline else None, width=outlineWidth)
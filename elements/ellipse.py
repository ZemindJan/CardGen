from PIL import Image
from core.alignment import Alignment
from elements.element import CardElement
from core.geometry import Point, Rect
from core.color import RGBA, Color
from core.schema import Schema
from PIL import ImageDraw
from elements.shape import ShapeElement, Outline

class EllipseElement(ShapeElement):
    def __init__(self, size: Point, fill: Color = None, offset: Point = None, alignment: Alignment = None, outline: Outline | None = None, children : list[CardElement] = None, visible : bool = True) -> None:
        super().__init__(
            size=size, 
            fill=fill, 
            offset=offset, 
            alignment=alignment, 
            outline=outline, 
            children=children, 
            visible=visible
        )

    def draw_shape(self, draw: ImageDraw.ImageDraw, area: Rect, fill: RGBA, outline: RGBA = None, outlineWidth: int = 0):
        draw.ellipse(xy=area.int_tuple(), fill=fill.tuple(), outline=outline.tuple() if outline else None, width=outlineWidth)
from PIL import Image
from core.alignment import Alignment
from elements.element import CardElement
from core.geometry import Point, Rect
from core.color import Color, make_color
from core.schema import Schema
from PIL import ImageDraw
from abc import abstractmethod

class ShapeElement(CardElement):
    def __init__(self, fill : Color, offset: Point, size: Point, alignment: Alignment = None, outline : Color = None, outlineWidth : int = 0, children : list[CardElement] = None) -> None:
        super().__init__(offset, alignment, size, children)
        self.fill = make_color(fill)
        self.outline = make_color(outline)
        self.outlineWidth = make_color(outlineWidth)
    
    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index : int = 0):
        area : Rect = self.calculate_size(parent_area)
        draw = ImageDraw.Draw(image)

        self.draw_shape(
            draw,
            area,
            self.fill,
            self.outline,
            self.outlineWidth
        )

        for child in self.children:
            child : CardElement
            child.draw(image, entry, schema, area)
    
    @abstractmethod
    def draw_shape(self, draw : ImageDraw.ImageDraw, area : Rect, fill : Color, outline : Color = None, outlineWidth : int = 0):
        pass
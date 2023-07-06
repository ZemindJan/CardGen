from PIL import Image
from core.alignment import Alignment
from elements.element import CardElement
from core.geometry import Point, Rect
from core.color import Color
from core.schema import Schema
from PIL import ImageDraw
from abc import abstractmethod

class ShapeElement(CardElement):
    def __init__(self, fill : Color, offset: Point, size: Point, alignment: Alignment = None, outline : Color = None, outlineWidth : int = 0) -> None:
        super().__init__(offset, alignment, size)
        self.fill = fill
        self.outline = outline
        self.outlineWidth = outlineWidth
    
    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect):
        area : Rect = self.calculate_size(parent_area)
        draw = ImageDraw.Draw(image)

        self.draw_shape(
            draw,
            area,
            self.fill,
            self.outline,
            self.outlineWidth
        )
    
    @abstractmethod
    def draw_shape(self, draw : ImageDraw.ImageDraw, area : Rect, fill : Color, outline : Color = None, outlineWidth : int = 0):
        pass
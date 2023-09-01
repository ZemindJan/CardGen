from PIL import Image
from core.alignment import Alignment
from elements.element import CardElement
from core.geometry import Point, Rect
from core.color import RGBA, Color, Colors, verify_color
from core.schema import Schema
from PIL import ImageDraw
from abc import abstractmethod
from dataclasses import dataclass

@dataclass
class Outline:
    color : Color
    width : int

class ShapeElement(CardElement):
    fill : RGBA
    outline : Outline | None

    def __init__(self, size: Point, fill : Color = None, offset: Point = None,  alignment: Alignment = None, outline : Outline | None = None, children : list[CardElement] = None, visible : bool = True) -> None:
        super().__init__(offset=offset, alignment=alignment, size=size, children=children, visible=visible)
        self.fill = verify_color(fill or Colors.Black)
        self.outline = outline
    
    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index : int = 0):
        area : Rect = self.calculate_size(parent_area)
        draw = ImageDraw.Draw(image)

        if self.visible:
            self.draw_shape(
                draw,
                area,
                self.fill,
                verify_color(self.outline.color) if self.outline else None,
                self.outline.width if self.outline else None,
            )

        for child in self.children:
            child : CardElement
            child.draw(image, entry, schema, area)
    
    @abstractmethod
    def draw_shape(self, draw : ImageDraw.ImageDraw, area : Rect, fill : RGBA, outline : RGBA = None, outlineWidth : int = 0):
        pass
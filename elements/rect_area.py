from PIL import Image
from core.alignment import Alignment
from elements.element import CardElement
from core.geometry import Point, Rect
from core.color import Color
from core.schema import Schema
from PIL import ImageDraw

class RectArea(CardElement):
    def __init__(self, color : Color, offset: Point = None, alignment: Alignment = None, size: Point = None) -> None:
        super().__init__(offset, alignment, size)
        self.color = color
    
    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect):
        area : Rect = self.calculate_size(parent_area)
        draw = ImageDraw.Draw(image)

        draw.rectangle(
            xy=area.int_tuple(),
            fill=self.color.tuple()
        )
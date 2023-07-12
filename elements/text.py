from PIL import Image
from core.alignment import Alignment
from core.geometry import Point, Rect
from core.schema import Schema
from elements.element import CardElement
from PIL import ImageDraw, ImageFont
from core.color import Color

class TextElement(CardElement):
    def __init__(self, text : str, font_path : str, fill : Color, text_size : int, offset: Point = None, alignment: Alignment = None, size: Point = None) -> None:
        super().__init__(offset, alignment, size)
        self.text = text
        self.font = font_path
        self.fill = fill
        self.text_size = text_size

    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect):
        draw = ImageDraw.Draw(image)
        area : Rect = self.calculate_size(parent_area)

        font = ImageFont.truetype(f'fonts/{self.font}', size=self.text_size)

        draw.fontmode = "L"

        draw.text(
            xy=area.int_tuple(),
            text=self.text,
            font=font,
            fill=self.fill.tuple(),
            align="center"
        )
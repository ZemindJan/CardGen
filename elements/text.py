from PIL import Image
from core.alignment import Alignment
from core.geometry import Point, Rect
from core.schema import Schema
from elements.element import CardElement
from PIL import ImageDraw, ImageFont
from core.color import Color
from core.string_parser import parse_string

class TextElement(CardElement):
    def __init__(self, text : str, font_path : str, fill : Color, text_size : int, offset: Point = None, alignment: Alignment = None) -> None:
        super().__init__(offset, alignment, None)
        self.text = text
        self.font = font_path
        self.fill = fill
        self.text_size = text_size

    

    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index : int = 0):
        draw = ImageDraw.Draw(image)
        text = parse_string(self.text, entry, index)

        # Set size
        font = ImageFont.truetype(f'fonts/{self.font}', size=self.text_size)
        x1, y1, x2, y2 = draw.textbbox(xy=(0, 0, 1000, 1000), text=text, font=font)
        self.size = Point(x2 - x1, y2 - y1)

        # Get area
        area : Rect = self.calculate_size(parent_area)

        draw.fontmode = "L"

        draw.text(
            xy=area.int_tuple(),
            text=text,
            font=font,
            fill=self.fill.tuple(),
            align="right"
        )
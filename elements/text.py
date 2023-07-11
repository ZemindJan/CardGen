from PIL import Image
from core.alignment import Alignment
from core.geometry import Point, Rect
from core.schema import Schema
from elements.element import CardElement

class TextElement(CardElement):
    def __init__(self, offset: Point = None, alignment: Alignment = None, size: Point = None) -> None:
        super().__init__(offset, alignment, size)

    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect):
        pass
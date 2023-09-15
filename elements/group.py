from PIL import Image
from core.alignment import Alignment
from core.geometry import Point, Rect
from core.schema import Schema
from core.scaling import PARENT
from elements.element import CardElement

class GroupElement(CardElement):
    def __init__(self, offset: Point = None, alignment: Alignment = None, size: Point = None, children: list[CardElement] = None, visible: bool = True) -> None:
        super().__init__(offset, alignment, size or Point(PARENT, PARENT), children, visible)

    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index: int = 0):
        if not self.visible:
            return
        
        for child in self.children:
            child.predraw(entry)
            child.draw(image, entry, schema, self.calculate_area(parent_area), index)
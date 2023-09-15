from PIL import Image
from core.alignment import Alignment
from core.geometry import Point, Rect
from core.schema import Schema
from core.scaling import PARENT
from elements.element import CardElement
from elements.group import GroupElement

class GridElement(GroupElement):
    def __init__(self, offset: Point = None, alignment: Alignment = None, size: Point = None, children: list[CardElement] = None, visible: bool = True) -> None:
        super().__init__(offset, alignment, size, children, visible)
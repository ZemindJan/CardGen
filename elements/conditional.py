from core.geometry import Point
from elements.element import ICardElement
from PIL import Image, ImageDraw
from core.schema import Schema
from abc import abstractmethod
from core.geometry import Point, Rect
from core.scaling import scale
from core.conditions import parse_condition

class ConditionalElement(ICardElement):
    def __init__(self, condition : str, on_true : list[ICardElement], on_false : list[ICardElement] = None) -> None:
        self.condition = parse_condition(condition)
        self.on_true = on_true
        self.on_false = on_false or []

    def draw(
        self,
        image : Image.Image, 
        entry : dict[str, str], 
        schema : Schema,
        parent_area : Rect,
        index : int = 0
    ):
        children = self.on_true if self.condition.eval(entry) else self.on_false

        for child in children:
            child.draw(image, entry, schema, parent_area, index)

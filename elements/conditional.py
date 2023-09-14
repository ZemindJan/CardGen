from core.geometry import Point
from elements.element import ICardElement
from PIL import Image, ImageDraw
from core.schema import Schema
from abc import abstractmethod
from core.geometry import Point, Rect
from core.scaling import scale
from core.conditions import parse_condition, Condition, Boolean

class ConditionalElement(ICardElement):
    def __init__(self, condition : str, on_true : list[ICardElement], on_false : list[ICardElement] = None) -> None:
        self.condition = parse_condition(condition)
        self.on_true = on_true
        self.on_false = on_false or []
        self.__else_conditions : list[tuple[Condition, list[ICardElement]]] = []

    def draw(
        self,
        image : Image.Image, 
        entry : dict[str, str], 
        schema : Schema,
        parent_area : Rect,
        index : int = 0
    ):
        children = self.__eval_children(entry=entry)

        for child in children:
            child.draw(image, entry, schema, parent_area, index)

    def __eval_children(self, entry : dict[str, str]) -> list[ICardElement]:
        if self.condition.eval(entry=entry):
            return self.on_true
        elif len(self.__else_conditions) > 0:
            for condition, elements in self.__else_conditions:
                if condition.eval(entry=entry):
                    return self.on_false + elements
        else:
            return self.on_false

    def else_if(self, condition : str, elements : list[ICardElement]) -> 'ConditionalElement':
        self.__else_conditions.append((parse_condition(condition), elements))

    def else_draw(self, elements : list[ICardElement]):
        self.__else_conditions.append((Boolean(True), elements))

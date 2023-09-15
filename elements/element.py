from __future__ import annotations
from PIL import Image, ImageDraw
from core.schema import Schema
from abc import abstractmethod
from core.geometry import Point, Rect
from core.alignment import Alignment
from core.scaling import scale
from typing import Callable
from core.text.string_parser import replace_references


class CardElement:
    offset : Point
    alignment : Alignment
    size : Point
    children : list[CardElement]
    __on_write_entry_fns : list[Callable[[CardElement, dict[str, str]], None]]

    def __init__(self, offset : Point = None, alignment : Alignment = None, size : Point = None, children : list[CardElement] = None, visible : bool = True) -> None:
        self.offset = offset or Point.zero()
        self.alignment = alignment or Alignment.TOP_LEFT
        self.size = size or Point.zero()
        self.children = children or []
        self.visible = visible
        self.__on_write_entry_fns = []

    def calculate_area(self, parent_area : Rect) -> Rect:
        origin = self.alignment.get_root(parent_area)

        scaled_offset = scale(self.offset, parent_area.size())
        scaled_size = scale(self.size, parent_area.size())

        alignment_offset = self.alignment.get_root(Point.zero().to(scaled_size))
        return Rect(origin + scaled_offset - alignment_offset, origin + scaled_offset + scaled_size - alignment_offset)

    @abstractmethod
    def draw(
        self,
        image : Image.Image, 
        entry : dict[str, str], 
        schema : Schema,
        parent_area : Rect,
        index : int = 0
    ):
        pass

    def predraw(self, entry : dict[str, str]) -> None:
        for modifier in self.__on_write_entry_fns:
            modifier(self, entry)

    def on_draw(self, modifier : Callable[['CardElement', dict[str, str]], None]) -> 'CardElement':
        self.__on_write_entry_fns.append(modifier)

        return self

    def on_draw_set_fields(self, **kwargs) -> 'CardElement':
        def fn(element : 'CardElement', entry : dict[str, str]):
            for key, value in kwargs.items():
                setattr(element, replace_references(key, entry), replace_references(value, entry))

        self.__on_write_entry_fns.append(fn)

        return self
    
from PIL import Image, ImageDraw
from core.schema import Schema
from abc import abstractmethod
from core.geometry import Point, Rect
from core.alignment import Alignment, TopLeft
from core.scaling import scale

<<<<<<< HEAD
=======
class ICardElement:
    def draw(
        self,
        image : Image.Image, 
        entry : dict[str, str], 
        schema : Schema,
        parent_area : Rect,
        index : int = 0
    ):
        pass

>>>>>>> 35a26814e02ad28777518213a06d6d1ff5e5121c
class CardElement:
    def __init__(self, offset : Point = None, alignment : Alignment = None, size : Point = None, children : list = None) -> None:
        self.offset = offset or Point.zero()
        self.alignment = alignment or TopLeft
        self.size = size or Point.zero()
        self.children = children or []
<<<<<<< HEAD
=======
        self.visible = True
>>>>>>> 35a26814e02ad28777518213a06d6d1ff5e5121c

    def calculate_size(self, parent_area : Rect) -> Rect:
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
<<<<<<< HEAD
        pass
=======
        pass

    def set_invisible(self):
        self.visible = False
        return self
>>>>>>> 35a26814e02ad28777518213a06d6d1ff5e5121c

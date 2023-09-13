from PIL import Image, ImageOps
from core.alignment import Alignment
from core.geometry import Point, Rect
from core.schema import Schema
from core.safe_paste import safe_paste
from elements.element import CardElement

class MirrorElement(CardElement):
    def __init__(self, 
                 mirror_x : bool = True,
                 mirror_y : bool = True,
                 offset: Point = None, 
                 alignment: Alignment = None, 
                 size: Point = None, children: 
                 list = None) -> None:
        super().__init__(offset=offset, alignment=alignment, size=size, children=children, visible=True)
        self.mirror_x = mirror_x
        self.mirror_y = mirror_y

    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index: int = 0):
        area = self.calculate_area(parent_area)

        my_image = Image.new(mode='RGBA', size=area.size().int_tuple())

        for child in self.children:
            child.draw(my_image, entry, schema, Rect(Point.zero(), area.size()), index)

        if self.mirror_x:
            my_image = ImageOps.mirror(my_image)
        if self.mirror_y:
            my_image = ImageOps.flip(my_image)

        safe_paste(image, my_image, area)
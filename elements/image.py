from PIL import Image, ImageDraw, ImageFont
from core.alignment import Alignment
from core.geometry import Point, Rect
from core.schema import Schema
from elements.element import CardElement
from settings import Settings

class ImageElement(CardElement):

    def __init__(self, name : str, offset: Point = None, alignment: Alignment = None, size : Point = None, children: list = None, visible : bool = True) -> None:
        super().__init__(offset=offset, alignment=alignment, size=size, children=children, visible=visible)
        
        self.my_image = Image.open(f'{Settings.ImagesDirectory}/{name}')
        
        if size is None:
            self.size = Point(*self.my_image.size)
        else:
            self.size = size


    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index: int = 0):
        if not self.visible:
            return

        area = self.calculate_size(parent_area)
        self.my_image = self.my_image.resize(area.size().int_tuple())
        image.paste(self.my_image, area.int_tuple(), self.my_image)
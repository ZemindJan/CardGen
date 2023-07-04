from core.geometry import Point, Rect
from core.color import Color, White
from PIL import Image, ImageDraw

DEFAULT_DIMENSIONS = Point(336, 240)

class Schema:
    def __init__(self, dimensions : Point = None, elements = None, background : Color = None) -> None:
        self.dimensions = dimensions or DEFAULT_DIMENSIONS
        self.elements   = elements   or []
        self.background = background or White

    def draw(self, entry : dict[str, str]):
        image = Image.new(
            mode='RGBA', 
            size=self.dimensions.int_tuple(), 
            color=self.background.tuple()
        )

        for element in self.elements:
            element.draw(image, entry, self, Point.zero().to(self.dimensions))

        image.save('test.png')
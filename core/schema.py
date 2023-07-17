from core.geometry import Point, Rect
from core.text.string_parser import replace_references
from core.color import Color, White
from PIL import Image, ImageDraw
from core.create_directories import verify_directories
from settings import Settings
from data.source import Source

DEFAULT_DIMENSIONS = Point(2.5 * 96 * 2, 3.5 * 96 * 2)

class Schema:
    def __init__(self, naming : str, dimensions : Point = None, elements = None, background : Color = None) -> None:
        self.naming = naming
        self.dimensions = dimensions or DEFAULT_DIMENSIONS
        self.elements   = elements   or []
        self.background = background or White

    def draw_card(self, entry : dict[str, str], index = 0):
        image = Image.new(
            mode='RGBA', 
            size=self.dimensions.int_tuple(), 
            color=self.background.tuple()
        )

        for element in self.elements:
            element.draw(image, entry, self, Point.zero().to(self.dimensions))

        path = f'{Settings.CardsDirectory}/{replace_references(self.naming, entry, index)}.png'
        verify_directories(path)
        image.save(path)

    def process(self, source : Source):
        entries = source.get_data()
        for index, entry in enumerate(entries):
            self.draw_card(entry, index)
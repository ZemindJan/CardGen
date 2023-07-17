from core.color import Color, make_color
from core.geometry import Point
from core.text.tag import Tag
from core.text.fonts import get_font

from PIL import Image, ImageDraw, ImageFont
from icon_atlas import icon_paths
from settings import Settings

def get_icon_path(name):
    return icon_paths[name]

class IconSegment:
    def __init__(self, name : str, max_icon_size : Point) -> None:
        self.image = Image.open(f'{Settings.IconsDirectory}/{get_icon_path(name)}')
        self.name = name
        self.max_icon_size = max_icon_size
        size = Point(*self.image.size)
        scale_diff = max(size.x / max_icon_size.x, size.y / max_icon_size.y)
        self.image = self.image.resize((int(size.x / scale_diff), int(size.y / scale_diff)))
        self.size = Point(*self.image.size)

    def draw(self, coords : Point, line_size : Point, image : Image.Image):
        whitespace = line_size.y - self.size.y
        my_coords = coords + Point.y_span(whitespace / 2)
        image.paste(self.image, my_coords.to(my_coords + self.size).int_tuple(), self.image)
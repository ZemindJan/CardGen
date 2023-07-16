from core.color import Color
from core.geometry import Point
from core.text.tag import Tag


from PIL import ImageDraw, ImageFont


class TextSegment:
    def __init__(self, content : str, font : str, font_size : int, fill : Color, tags : list[Tag]) -> None:
        self.content = content
        self.tags = tags
        self.font = font
        self.font_size = font_size
        self.fill = fill
        self.apply_tags()
        self.size = self.calculate_size()

    def apply_tags(self):
        for tag in self.tags:
            if tag.name == 'font':
                self.font = tag.data
            if tag.name == 'size':
                self.font_size = int(tag.data)

    def __repr__(self) -> str:
        content = self.content
        prefix = ''
        suffix = ''

        for tag in self.tags:
            prefix += tag.opening_repr()
            suffix += tag.closing_repr()

        return f'{prefix}{content}{suffix}'

    def draw(self, coords : Point, line_size : Point, draw : ImageDraw.ImageDraw):
        font = ImageFont.truetype(f'fonts/{self.font}', size=self.font_size)
        draw.fontmode = "L"

        my_coords = coords + Point.y_span(self.calculate_y_offset(line_size))

        draw.text(
            xy=my_coords.to(Point(1000, 1000)).int_tuple(),
            text=self.content,
            font=font,
            fill=self.fill.tuple(),
        )

    def calculate_y_offset(self, line_size : Point) -> int:
        font = ImageFont.truetype(f'fonts/{self.font}', size=self.font_size)
        x1, y1, x2, y2 = font.getbbox('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        whitespace = line_size.y - (y2 - y1)
        return whitespace

    def calculate_size(self) -> Point:
        font = ImageFont.truetype(f'fonts/{self.font}', size=self.font_size)
        x1, y1, x2, y2 = font.getbbox(self.content)
        return Point(x2 - x1, y2 - y1)
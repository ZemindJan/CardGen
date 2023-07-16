from PIL import Image
from core.alignment import Alignment, middle_y_align, center_x_align, right_x_align, bottom_y_align
from core.geometry import Point, Rect
from core.schema import Schema
from core.text.segment import TextSegment
from elements.element import CardElement
from PIL import ImageDraw, ImageFont
from core.color import Color, make_color
from core.text.string_parser import parse_string, newline
from core.text.line import make_lines
from core.text.fonts import get_font

class TextElement(CardElement):
    def __init__(self, text : str, font_path : str, fill : Color, font_size : int, line_spacing : int = 5, max_line_length : int = None, offset: Point = None, alignment: Alignment = None) -> None:
        super().__init__(offset, alignment, None)

        if not isinstance(fill, Color):
            fill = make_color(fill)

        self.text = text
        self.font = font_path
        self.fill = fill
        self.font_size = font_size
        self.max_line_length = max_line_length
        self.line_spacing = line_spacing

    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index : int = 0):
        draw = ImageDraw.Draw(image)
        elements = parse_string(self.text, self.font, self.font_size, self.fill, entry, index)

        font = get_font(self.font, self.font_size, [])
        space_size = font.getlength(' ')

        max_line_length = self.max_line_length
        if max_line_length is None:
            max_line_length = parent_area.size().x

        lines = make_lines(elements, self.font, self.font_size, max_line_length, space_size)
        total_height = sum(line.y_size for line in lines) + (len(lines) - 1) * self.line_spacing

        y_offset = 0
        y_whitespace = parent_area.size().y - total_height

        if self.alignment.y_align == middle_y_align:
            y_offset += y_whitespace / 2
        elif self.alignment.y_align == bottom_y_align:
            y_offset += y_whitespace

        for line in lines:
            x_whitespace = parent_area.size().x - line.x_size
            x_offset = 0
            
            if self.alignment.x_align == center_x_align:
                x_offset = x_whitespace / 2
            elif self.alignment.x_align == right_x_align:
                x_offset = x_whitespace 
            
            for segment in line.segments:
                segment.draw(Point(parent_area.p1.x + x_offset, parent_area.p1.y + y_offset), Point(line.x_size, line.y_size), draw)

                x_offset += segment.size.x + space_size

            y_offset += line.y_size + self.line_spacing


        
    
    

            



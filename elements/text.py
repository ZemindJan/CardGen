from PIL import Image
from core.alignment import Alignment, YAlignment, XAlignment
from core.geometry import Point, Rect
from core.schema import Schema
from core.text.segment.text import TextSegment
from elements.element import CardElement
from PIL import ImageDraw, ImageFont
from core.color import RGBA, verify_color, Color
from core.text.string_parser import parse_string, newline
from core.text.line import make_lines
from core.text.fonts import get_font

class TextElement(CardElement):
    text : str
    font : str
    max_icon_size : Point | None
    fill : RGBA
    font_size : int
    line_spacing : int
    max_line_length : int | None
    line_alignment : YAlignment

    def __init__(self, 
                 text : str, 
                 font_path : str, 
                 fill : Color, 
                 font_size : int, 
                 line_spacing : int = 5, 
                 max_line_length : int = None, 
                 offset: Point = None, 
                 alignment: Alignment = None, 
                 max_icon_size : Point = None,
                 line_alignment : YAlignment = None,
                 visible : bool = True) -> None:
        super().__init__(offset=offset, alignment=alignment, size=None, children=None, visible=vars)
        self.text = text
        self.font = font_path
        self.fill = verify_color(fill)
        self.font_size = font_size
        self.max_line_length = max_line_length
        self.line_spacing = line_spacing
        self.max_icon_size = max_icon_size
        self.line_alignment = line_alignment or YAlignment.BOTTOM

    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index : int = 0):
        if not self.visible:
            return
        
        size = self.font_size

        while True:
            elements = parse_string(self.text, self.font, size, self.fill, self.max_icon_size, entry, index)

            font = get_font(self.font, size, [])
            space_size = font.getlength(' ')

            max_line_length = self.max_line_length
            if max_line_length is None:
                max_line_length = parent_area.size().x

            

            lines = make_lines(elements, self.font, size, max_line_length, space_size)
            total_height = sum(line.y_size for line in lines) + (len(lines) - 1) * self.line_spacing

            y_offset = self.offset.y
            y_whitespace = parent_area.size().y - total_height
            x_whitespace = parent_area.size().x - max(line.x_size for line in lines)

            x_whitespace = max(line.x_size for line in lines)

            if y_whitespace >= 0 and x_whitespace >= 0:
                break
            elif size < 10:
                break
            elif all(line.tallest_is_icon() for line in lines):
                break
            else:
                size = min(int(size * 0.9), int(size - 3))

        if self.alignment.y == YAlignment.MIDDLE:
            y_offset += y_whitespace / 2
        elif self.alignment.y == YAlignment.BOTTOM:
            y_offset += y_whitespace

        for line in lines:
            x_whitespace = parent_area.size().x - line.x_size
            x_offset = self.offset.x
            
            if self.alignment.x == XAlignment.CENTER:
                x_offset += x_whitespace / 2
            elif self.alignment.x == XAlignment.RIGHT:
                x_offset += x_whitespace 
            
            for segment in line.segments:
                segment.draw(Point(parent_area.p1.x + x_offset, parent_area.p1.y + y_offset), Point(line.x_size, line.y_size), image, self.line_alignment)

                x_offset += segment.size.x + space_size

            y_offset += line.y_size + self.line_spacing


        
    
    

            



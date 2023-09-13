from core.geometry import Point
from PIL import ImageDraw, ImageFont, Image
from core.text.segment.line import LineSegment
from core.text.segment.icon import IconSegment
from core.text.string_parser import newline
from typing import Literal

class TextLine:
    def __init__(self, segments : list[LineSegment], x_size : int, y_size : int) -> None:
        self.segments = segments
        self.x_size = x_size
        self.y_size = y_size

    def tallest_is_icon(self) -> bool:
        tallest = None
        height = -1

        for segment in self.segments:
            if segment.size.y > height:
                tallest = segment
                height = segment.size.y

        return isinstance(tallest, IconSegment)

def make_lines(elements : list[LineSegment | Literal['newline']], font : str, font_size : int, max_line_length : int, space_size : int) -> list[TextLine]:
    lines = []
    line = []
    line_size = 0
    line_max_y = 0
    longest_line = 0

    def push():
        nonlocal lines
        nonlocal line
        nonlocal line_size
        nonlocal longest_line
        nonlocal line_max_y

        if line_size > longest_line:
            longest_line = line_size

        lines.append(TextLine(line, line_size, line_max_y))
        line = []
        line_size = 0
        line_max_y = 0

    for element in elements:
        if element == newline:
            push()
            continue
        
        element_size = element.size
        
        if len(line) == 0:
            line.append(element)
            line_size += element_size.x
            line_max_y = element_size.y
            continue

        if line_size + space_size + element_size.x > max_line_length:
            push()
            line.append(element)
            line_size += element_size.x
            line_max_y = element_size.y
            continue

        line.append(element)
        line_size += space_size + element_size.x

        if line_max_y < element_size.y:
            line_max_y = element_size.y

    push()
    return lines

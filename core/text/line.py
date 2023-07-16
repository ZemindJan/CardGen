from core.geometry import Point
from PIL import ImageDraw, ImageFont, Image
from core.color import Black
from core.text.segment import TextSegment
from core.text.string_parser import newline

class TextLine:
    def __init__(self, segments : list[TextSegment], x_size : int, y_size : int) -> None:
        self.segments = segments
        self.x_size = x_size
        self.y_size = y_size

def make_lines(elements : list[TextSegment], font : str, font_size : int, max_line_length : int, space_size : int) -> list[TextLine]:
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

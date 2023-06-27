from PIL import Image, ImageFont, ImageDraw
from dimensions import icon_size, inner_rect, card_size, line_spacing, icon_x_buffer, icon_y_offset
from text.icons import *
from fonts import font
from colors import BLACK, GOLD

LINEBREAK = '.'

class Text:
    content : str
    font : ImageFont.FreeTypeFont

    def __init__(self, content : str):
        self.content = content
        self.font = font

    def is_icon(self):
        return False

    def get_length(self):
        return font.getlength(self.content) + 2 * icon_x_buffer

class Icon:
    name : str
    image : Image.Image

    def __init__(self, name : str) -> None:
        if name.startswith(icon_prefix):
            name = name.replace(icon_prefix, '').lower()

        self.name = name
        self.image = Image.open(get_icon_file(name)).resize(icon_size.tuple())

    def is_icon(self):
        return True
    
    def get_length(self):
        return icon_size.x

def process(text : str) -> list[Text | Icon | str]:
    elements = []
    curr_string = ''
    is_icon = False

    def push():
        nonlocal curr_string
        nonlocal is_icon

        if curr_string == '':
            return

        if is_icon:
            elements.append(Icon(curr_string))
        else:
            elements.append(Text(curr_string))

        curr_string = ''
        is_icon = False

    for char in text:
        if char == LINEBREAK:
            push()
            elements.append(LINEBREAK)
        elif char == ' ' and curr_string == '':
            continue
        elif char == icon_prefix:
            push()
            is_icon = True
        elif char == ' ' and is_icon:
            push()
        else:
            curr_string += char
    
    push()

    # don't want trailing linebreak
    if elements[-1] == LINEBREAK:
        elements.pop()

    return elements

def write_text(text : list[Text | Icon | str], image : Image.Image, draw : ImageDraw.ImageDraw):
    # Split by lines
    lines = []

    curr_line = []
    while len(text) > 0:
        item = text.pop(0)

        if item == LINEBREAK:
            lines.append(curr_line.copy())
            curr_line.clear()
        else:
            curr_line.append(item)

    if len(curr_line) > 0:
        lines.append(curr_line)
    
    # Write Lines
    for i, line in enumerate(lines):
        write_line(line, image, draw, i, len(lines))

def write_line(text : list[Text | Icon | str], image : Image.Image, draw : ImageDraw.ImageDraw, lineNum : int, totalLines : int):
    length = 0
    x_offsets = [0 for _ in text]

    for i, item in enumerate(text):
        length += item.get_length()
        
        for j in range(i, len(text)):
            x_offsets[j] += item.get_length()
    
    x_origin = (card_size.x // 2) - length // 2
    mid_pos = totalLines / 2
    y_position = int( (lineNum - mid_pos) * line_spacing + (inner_rect.p1.y + inner_rect.p2.y) // 2 )

    for i, item in enumerate(text):
        x_position = int(x_origin + x_offsets[i - 1]) if i > 0 else int(x_origin)
        
        if isinstance(item, Icon):
            image.paste(item.image, (x_position + icon_x_buffer - icon_size.x // 2, y_position + icon_y_offset, x_position + icon_x_buffer + icon_size.x // 2, y_position + icon_size.y + icon_y_offset), item.image)
        else:
            item : Text
            draw.text((x_position, y_position), item.content, font=item.font, fill=BLACK)
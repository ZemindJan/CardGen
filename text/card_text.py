from PIL import Image, ImageFont, ImageDraw
from dimensions import inner_rect
from text.icons import *

LINEBREAK = '.'

class Text:
    content : str
    font : ImageFont.FreeTypeFont

    def Text(content : str):
        pass

class Icon:
    name : str
    image : Image.Image

    def Icon(name : str):
        pass

class CardText:
    content : list[Text | Icon | str]

    def __init__(self, content : list[Text | Icon | str]) -> None:
        self.content = content

def Process(text : str) -> CardText:
    elements = []
    curr_string = ''
    is_icon = False

    def push():
        if curr_string == '':
            return

        if is_icon:
            elements.append(Icon(curr_string))
        else:
            elements.append(Text(curr_string))

        curr_string = ''

    for char in text:
        if char == LINEBREAK:
            push()
            elements.append(LINEBREAK)
        elif char == icon_prefix:
            is_icon = True
        elif char == ' ':
            push()
        else:
            curr_string += char
    
    push()

    return CardText(elements)

def WriteText(text : CardText, image : Image.Image, draw : ImageDraw):
    # Split by lines
    lines = []

    curr_line = []
    while len(text.content) > 0:
        item = text.content.pop(0)

        if item == LINEBREAK:
            lines.append(curr_line.copy())
            curr_line.clear()
        else:
            curr_line.append(item)

    if len(curr_line) > 0:
        lines.append(curr_line)
    
    # Write Lines
    for i, line in enumerate(lines):
        WriteLine(CardText(line), image, draw, i, len(lines))

def WriteLine(text : CardText, image : Image.Image, draw : ImageDraw, lineNum : int, totalLines : int):
    pass

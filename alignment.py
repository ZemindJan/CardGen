from colors import *
from geometry import Vec2, Rect
from PIL import ImageDraw, ImageFont

LEFT = 'LEFT'
TOP = 'TOP'
CENTER = 'CENTER'
BOTTOM = 'BOTTOM'
RIGHT = 'RIGHT'

def center_text(draw : ImageDraw.ImageDraw, font : ImageFont.FreeTypeFont, text : str, width : int) -> str:
    _, _, space_width, _ = draw.textbbox((0, 0), ' ', font=font)

    lines = text.split('\n')
    final = ''

    for line in lines:
        _, _, line_length, _ = draw.textbbox((0, 0), line, font=font)

        make_up = width - line_length
        num_spaces = int(make_up / space_width)

        final += line.center(len(line) + num_spaces) + '\n'
    
    return final

def write(text : str, draw : ImageDraw.ImageDraw, font : ImageFont.FreeTypeFont, area : Rect, x_align = LEFT, y_align = TOP, fill=BLACK):
    _, _, w, h = draw.textbbox((0, 0), text, font=font)

    size = area.size()
    x = area.p1.x

    if x_align == CENTER:
        x += (size.x - w) / 2
        text = center_text(draw, font, text, w)
    if x_align == RIGHT:
        x += size.x - w
    
    y = area.p1.y

    if y_align == CENTER:
        y += (size.y - h) / 2
    if y_align == BOTTOM:
        y += size.y - h

    draw.text((x, y), text, font=font, fill=fill)
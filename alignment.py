from colors import *
from geometry import Vec2
from PIL import ImageDraw, ImageFont

LEFT = 'LEFT'
TOP = 'TOP'
CENTER = 'CENTER'
BOTTOM = 'BOTTOM'
RIGHT = 'RIGHT'

def write(size, draw : ImageDraw.ImageDraw, font, x_align = LEFT, y_align = TOP):
    _, _, w, h = draw.textbbox((0, 0), 'ZEUS', font=font)

    x = 0


    draw.text(((size.x - w)/2, 20), 'ZEUS', font=font, fill=BLACK)
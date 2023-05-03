from PIL import Image, ImageFont, ImageDraw
from geometry import Vec2
from colors import *
from alignment import write

ratio = Vec2(2.5, 3.5)
scale = 100
size = (ratio * scale).to_ints()
image = Image.new('RGBA', size=size.tuple(), color=WHITE)
font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Bold.ttf', size=32)
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, size.x, size.y / 5), BLUE)
draw.rectangle((0, 0, size.x / 20, size.y), BLUE)
draw.rectangle((0, size.y - size.y / 20, size.x, size.y), BLUE)
draw.rectangle((size.x - size.x / 20, 0, size.x, size.y), BLUE)


write(size, draw, font)




image.save('out/test.png')
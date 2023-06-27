from PIL import Image, ImageDraw
from geometry import Vec2, Rect
from colors import *
from text.alignment import write, LEFT, CENTER, TOP, BOTTOM
from card import Card
import os
from fonts import *
from text.card_text import process, write_text
from settings import Settings

ratio = Vec2(2.5, 3.5)
scale = 100
size = (ratio * scale).to_ints()

CARDS_DIR = 'out/cards'
DECKS_DIR = 'out/decks'
ALL_DIRS = (CARDS_DIR, DECKS_DIR)

for path in ALL_DIRS:
    if not os.path.exists(path):
        os.makedirs(path)

top_frame_size = int(size.y / 5)
side_frame_size = int(size.x / 20)
bottom_frame_size = int(size.y / 20)

FRAME_THICKNESS = int(size.x / 40)

SPEED_TRIANGLE_LOCATION = Vec2(size.x / 2, size.y)
SPEED_TRIANGLE_SIZE = Vec2(size.x / 4, size.y / 8)
SUITE_SIZE = Vec2(size.x * 2 // 7, size.x * 2 // 7)



SUITE_IMAGES = {
    ROCK : 'assets/suites/Stone Suite.png',
    PAPER: 'assets/suites/Scrolls Suite.png',
    SCISSORS: 'assets/suites/Blades Suite.png',
}

def generate_card(card: Card):
    image = Image.new('RGBA', size=size.tuple(), color=WHITE)
    draw = ImageDraw.Draw(image)

    background_color = BACKGROUNDS[card.suite]

    # Frames
    draw.rectangle((0, 0, size.x, top_frame_size), background_color)
    draw.rectangle((0, 0, side_frame_size, size.y), background_color)
    draw.rectangle((0, size.y - bottom_frame_size,
                   size.x, size.y), background_color)
    draw.rectangle((size.x - side_frame_size, 0,
                   size.x, size.y), background_color)
    
    draw.rectangle((side_frame_size, top_frame_size, 
                    size.x - 1 * side_frame_size, size.y - bottom_frame_size), GOLD)
    draw.rectangle((side_frame_size + FRAME_THICKNESS, top_frame_size + FRAME_THICKNESS, 
                    size.x - 1 * side_frame_size - FRAME_THICKNESS, size.y - bottom_frame_size - FRAME_THICKNESS), WHITE)

    # Title
    title_area = Rect(Vec2(side_frame_size, 0), Vec2(size.x, int(top_frame_size * 0.5)))
    subtitle_area = Rect(Vec2(side_frame_size, int(top_frame_size * 1/2)),
                         Vec2(size.x, top_frame_size * 0.8))
    write_area = Rect(Vec2(side_frame_size, top_frame_size), Vec2(
        size.x - side_frame_size, size.y - bottom_frame_size))

    
    write_text(process(card.effect), image, draw)

    write(card.name, draw, title_font, title_area,
          x_align=LEFT, y_align=BOTTOM)
    write(card.god, draw, subtitle_font,
          subtitle_area, x_align=LEFT, y_align=BOTTOM)
    #write(preprocess_effect(card.Effect), draw, font,
    #      write_area, x_align=CENTER, y_align=CENTER)

    
    if Settings.use_speed_value:
        add_speed_triangle(card, draw)
    
    add_suite(image, card)

    image.save(f'{CARDS_DIR}/{card.name}.png')


def add_speed_triangle(card: Card, draw: ImageDraw):
    write_area = Rect(
        SPEED_TRIANGLE_LOCATION -
        Vec2(SPEED_TRIANGLE_SIZE.x / 2, SPEED_TRIANGLE_SIZE.y),
        SPEED_TRIANGLE_LOCATION + Vec2(SPEED_TRIANGLE_SIZE.x / 2, 0)
    )
    
    draw.polygon([
        (SPEED_TRIANGLE_LOCATION.x - SPEED_TRIANGLE_SIZE.x / 2,
         SPEED_TRIANGLE_LOCATION.y),
        (SPEED_TRIANGLE_LOCATION.x + SPEED_TRIANGLE_SIZE.x / 2,
         SPEED_TRIANGLE_LOCATION.y),
        (SPEED_TRIANGLE_LOCATION.x,
         SPEED_TRIANGLE_LOCATION.y - SPEED_TRIANGLE_SIZE.y)
    ], fill=GOLD)

    write(
        text=f'{card.speed}',
        draw=draw,
        font=speed_font,
        area=write_area,
        x_align=CENTER,
        y_align=CENTER,
    )

def add_suite(image : Image.Image, card : Card):
    suite_image = Image.open(SUITE_IMAGES[card.suite])
    suite_image = suite_image.resize(SUITE_SIZE.tuple())
    image.paste(suite_image, (size.x - SUITE_SIZE.x, 0, size.x, SUITE_SIZE.y), suite_image)

def generate_back():
    image = Image.new('RGBA', size=size.tuple(), color=WHITE)
    draw = ImageDraw.Draw(image)

    area = Rect(Vec2(0, 0), size)

    write('?', draw, bold_font, area, CENTER, CENTER)

    image.save(f'{CARDS_DIR}/back.png')

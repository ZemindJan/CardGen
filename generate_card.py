from PIL import Image, ImageFont, ImageDraw
from geometry import Vec2, Rect
from colors import *
from alignment import write, LEFT, CENTER
from card import Card
from text_processing import preprocess_effect
import os

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

def generate_card(card : Card):
    image = Image.new('RGBA', size=size.tuple(), color=WHITE)
    title_font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Bold.ttf', size=32)
    subtitle_font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Italic.ttf', size=20)
    font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Regular.ttf', size=18)
    bold_font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Bold.ttf', size=16)
    draw = ImageDraw.Draw(image)

    background_color = BACKGROUNDS[card.Type]

    # Frames
    draw.rectangle((0, 0, size.x, top_frame_size), background_color)
    draw.rectangle((0, 0, side_frame_size, size.y), background_color)
    draw.rectangle((0, size.y - bottom_frame_size, size.x, size.y), background_color)
    draw.rectangle((size.x - side_frame_size, 0, size.x, size.y), background_color)

    # Title
    title_area = Rect(Vec2(0, 0), Vec2(size.x, int(top_frame_size * 2/3)))
    subtitle_area = Rect(Vec2(0, int(top_frame_size * 2/3)), Vec2(size.x, top_frame_size))
    write_area = Rect(Vec2(side_frame_size, top_frame_size), Vec2(size.x - side_frame_size, size.y - bottom_frame_size))

    top_write_area = Rect(write_area.p1, Vec2(write_area.p2.x, write_area.size().y / 2 + write_area.p1.y))
    bottom_write_area  = Rect(Vec2(write_area.p1.x, write_area.size().y / 2 + write_area.p1.y), write_area.p2)

    write(card.Name, draw, title_font, title_area, x_align=CENTER, y_align=CENTER)
    write(card.Title, draw, subtitle_font, subtitle_area, x_align=CENTER, y_align=CENTER)
    write(preprocess_effect(card.Effect), draw, font, write_area, x_align=CENTER, y_align=CENTER)

    image.save(f'{CARDS_DIR}/{card.Name}.png')

def generate_back():
    image = Image.new('RGBA', size=size.tuple(), color=WHITE)
    bold_font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Bold.ttf', size=200)
    draw = ImageDraw.Draw(image)

    area = Rect(Vec2(0, 0), size)

    write('?', draw, bold_font, area, CENTER, CENTER)

    image.save(f'{CARDS_DIR}/back.png')

def generate_deck(name : str, cards : list[Card]):
    files = [f'{CARDS_DIR}/{card.Name}.png' for card in cards]

    Y_GRID_SIZE = 2
    X_GRID_SIZE = (len(cards) + 1) // 2

    new_image = Image.new('RGBA', size=(size.x * X_GRID_SIZE, size.y * Y_GRID_SIZE))

    for i, file in enumerate(files):
        x_coord = i // 2
        y_coord = i % 2

        image = Image.open(file)
        new_image.paste(image, (size.x * x_coord, size.y * y_coord, size.x * (x_coord + 1), size.y * (y_coord + 1))) 
        # Because minimum exports are 2 high, we double the height
    
    new_image.save(f'{DECKS_DIR}/{name}.png')


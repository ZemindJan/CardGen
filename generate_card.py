from PIL import Image, ImageFont, ImageDraw
from geometry import Vec2, Rect
from colors import *
from alignment import write, LEFT, CENTER
from card import Card
from text_processing import preprocess_effect

ratio = Vec2(2.5, 3.5)
scale = 100
size = (ratio * scale).to_ints()

CARDS_DIR = 'out/cards'
DECKS_DIR = 'out/decks'

top_frame_size = int(size.y / 5)
side_frame_size = int(size.x / 20)
bottom_frame_size = int(size.y / 20)

def generate_card(card : Card):
    image = Image.new('RGBA', size=size.tuple(), color=WHITE)
    title_font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Bold.ttf', size=32)
    font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Regular.ttf', size=16)
    bold_font = ImageFont.FreeTypeFont('fonts/AlegreyaSans-Bold.ttf', size=16)
    draw = ImageDraw.Draw(image)

    background_color = BACKGROUNDS[card.Type]

    # Frames
    draw.rectangle((0, 0, size.x, top_frame_size), background_color)
    draw.rectangle((0, 0, side_frame_size, size.y), background_color)
    draw.rectangle((0, size.y - bottom_frame_size, size.x, size.y), background_color)
    draw.rectangle((size.x - side_frame_size, 0, size.x, size.y), background_color)

    # Title
    title_area = Rect(Vec2(0, 0), Vec2(size.x, top_frame_size))
    write_area = Rect(Vec2(side_frame_size, top_frame_size), Vec2(size.x - side_frame_size, size.y - bottom_frame_size))

    top_write_area = Rect(write_area.p1, Vec2(write_area.p2.x, write_area.size().y / 2 + write_area.p1.y))
    bottom_write_area  = Rect(Vec2(write_area.p1.x, write_area.size().y / 2 + write_area.p1.y), write_area.p2)

    write(card.Name, draw, title_font, title_area, x_align=CENTER, y_align=CENTER)
    # write('Stun 1', draw, font, write_area, x_align=CENTER, y_align=CENTER)
    write(preprocess_effect(card.BaseEffect), draw, font, top_write_area, x_align=CENTER, y_align=CENTER)
    write('On Win:', draw, bold_font, write_area, CENTER, CENTER)
    write(preprocess_effect(card.ExtraWinEffect), draw, font, bottom_write_area, x_align=CENTER, y_align=CENTER)

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
    files.append(f'{CARDS_DIR}/back.png')

    new_image = Image.new('RGBA', size=(size.x * len(files), size.y))

    for i, file in enumerate(files):
        image = Image.open(file)
        new_image.paste(image, (size.x * i, 0, size.x * (i + 1), size.y))
    
    new_image.save(f'{DECKS_DIR}/{name}.png')


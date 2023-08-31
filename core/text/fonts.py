from core.color import RGBA, make_color
from core.text.tag import Tag
from PIL import ImageDraw, ImageFont
from font_atlas import transformations, transformation_tags, paths
from settings import Settings

def get_font(font : str, font_size : int, tags : list[Tag]):
    for tag in tags:
        if tag.name in transformation_tags:
            font_mapping = transformations[tag.name]
            if font in font_mapping:
                font = font_mapping[font]
            else:
                print(f'Warning: Font {font} does not have a variant defined for <{tag.name}>!')

    if font in paths:
        font = paths[font]

    return ImageFont.truetype(f'{Settings.FontsDirectory}/{font}', size=font_size)
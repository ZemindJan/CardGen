# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('4.2')

from cardsmith import *
from data.source import OnlineSource, ManualSource
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from elements.image import ImageElement
from settings import Settings
from elements.shape import Outline
from elements.mirror import MirrorElement
from keywords import preprocess_fields
from elements.group import GroupElement
from elements.grid import GridElement

Settings.CardsDirectory = 'out/props/4.2'

CARD_HEIGHT = int(4.75 * 96 * 2)
CARD_WIDTH = int(2.75 * 96 * 2)
CARD_SIZE = Point(CARD_WIDTH, CARD_HEIGHT)

SLOTS = 7

schema = Schema(
    dimensions=Point(CARD_WIDTH * 14, int(CARD_HEIGHT * 3.5)),
    naming='GameBoard',
    deck_name='crowd',
    elements=[
        # BACKGROUND
        RectElement(
            size=Point(PARENT, PARENT / 2),
            fill= 'champ_red',
        ),
        RectElement(
            size=Point(PARENT, PARENT / 2),
            offset=Point(0, PARENT / 2),
            fill= 'champ_blue'
        ),

        # CARD SLOTS
        GridElement(
            grid=[
                [
                    RectElement(
                        size=CARD_SIZE,
                        alignment=Alignment.MIDDLE_CENTER,
                        fill='card_red'
                    ) for _ in range(SLOTS)
                ],
                [
                    RectElement(
                        size=CARD_SIZE,
                        alignment=Alignment.MIDDLE_CENTER,
                        fill='card_blue'
                    ) for _ in range(SLOTS)
                ]
            ], 
            size=Point(CARD_SIZE.x * 9, PARENT),
            offset=Point(int(CARD_SIZE.x // 3 * 9), 0),
        ),

        # DISCARDS
        RectElement(
            size=CARD_SIZE,
            offset=Point(CARD_SIZE.x // 3 * 5, PARENT / 4 - CARD_SIZE.y // 2),
            fill='card_red',
            children=[
                MirrorElement(
                    size=Point(PARENT, PARENT),
                    children=[
                        RectElement(
                            size=Point(PARENT, PARENT),
                            fill='card_red',
                        ),
                        TextElement(
                            text='DISCARD',
                            font_path='alegreya_bold',
                            font_size=50,
                            fill='champ_red',
                            alignment=Alignment.MIDDLE_CENTER,
                        )
                    ]
                )
            ]
        ),
        RectElement(
            size=CARD_SIZE,
            offset=Point(CARD_SIZE.x // 3 * 5, PARENT * 3 / 4 - CARD_SIZE.y // 2),
            fill='card_blue',
            children=[
                TextElement(
                    text='DISCARD',
                    font_path='alegreya_bold',
                    font_size=50,
                    fill='champ_blue',
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),

        # EXHAUSTS
        RectElement(
            size=CARD_SIZE,
            offset=Point(CARD_SIZE.x // 3, PARENT / 4 - CARD_SIZE.y // 2),
            fill='grey',
            children=[
                MirrorElement(
                    size=Point(PARENT, PARENT),
                    children=[
                        RectElement(
                            size=Point(PARENT, PARENT),
                            fill='grey',
                        ),
                        TextElement(
                            text='EXHAUST',
                            font_path='alegreya_bold',
                            font_size=50,
                            fill='dark_grey',
                            alignment=Alignment.MIDDLE_CENTER,
                        )
                    ]
                )
            ]
        ),
        RectElement(
            size=CARD_SIZE,
            offset=Point(CARD_SIZE.x // 3, PARENT * 3 / 4 - CARD_SIZE.y // 2),
            fill='grey',
            children=[
                TextElement(
                    text='EXHAUST',
                    font_path='alegreya_bold',
                    font_size=50,
                    fill='dark_grey',
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),

        # DISCARDS
        RectElement(
            size=CARD_SIZE,
            offset=Point(CARD_SIZE.x // 3 * 37, PARENT / 4 - CARD_SIZE.y // 2),
            fill='card_red',
            children=[
                MirrorElement(
                    size=Point(PARENT, PARENT),
                    children=[
                        RectElement(
                            size=Point(PARENT, PARENT),
                            fill='card_red',
                        ),
                        TextElement(
                            text='DECK',
                            font_path='alegreya_bold',
                            font_size=50,
                            fill='champ_red',
                            alignment=Alignment.MIDDLE_CENTER,
                        )
                    ]
                )
            ]
        ),
        RectElement(
            size=CARD_SIZE,
            offset=Point(CARD_SIZE.x // 3 * 37, PARENT * 3 / 4 - CARD_SIZE.y // 2),
            fill='card_blue',
            children=[
                TextElement(
                    text='DECK',
                    font_path='alegreya_bold',
                    font_size=50,
                    fill='champ_blue',
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),
    ]
)

src = ManualSource([{}])
schema.process(src)
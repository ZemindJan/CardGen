# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\props')

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
from elements.grid import GridElement
from elements.group import GroupElement

Settings.CardsDirectory = 'out/props/4.2'

CARD_HEIGHT = int(3.5 * 96 * 2) // 2
CARD_WIDTH = int(2.5 * 96 * 2) // 2
CARD_SIZE = Point(CARD_WIDTH, CARD_HEIGHT)

SLOTS = 7

schema = Schema(
    dimensions=Point(CARD_WIDTH * 4, int(CARD_HEIGHT * 1.6)),
    naming='FavourBoard',
    deck_name='crowd',
    background='dark_favour',
    elements=[
        GridElement(
            grid=[[
                EllipseElement(
                    size=Point(80, 80),
                    alignment=Alignment.MIDDLE_CENTER,
                    offset=Point(PARENT / 10 * i, 20),
                    fill='favour' if 1 <= i <= 7 else 'darker_favour',
                    children=[
                        GroupElement() if 1 <= i <= 7 else
                        TextElement(
                            text='BLESSING',
                            alignment=Alignment.MIDDLE_CENTER,
                            font_path='alegreya',
                            font_size=20,
                            offset=Point(0, -3),
                            fill='favour',
                        )
                    ],
                )
                for i in range(9)
            ]],
            size=Point(PARENT - 80, 100)
        ),

        GridElement(
            size=Point(PARENT, PARENT - 100),
            offset=Point(0, 100),
            grid=[[
                RectElement(
                    size=CARD_SIZE,
                    fill='darker_favour',
                    alignment=Alignment.MIDDLE_CENTER,
                    children=[TextElement(
                        text='CROWD',
                        font_path='alegreya_bold',
                        font_size=50,
                        alignment=Alignment.MIDDLE_CENTER,
                        fill='favour',
                    )]
                ),

                RectElement(
                    size=CARD_SIZE,
                    fill='darker_favour',
                    alignment=Alignment.MIDDLE_CENTER,
                    children=[TextElement(
                        text='WHIM',
                        font_path='alegreya_bold',
                        font_size=50,
                        alignment=Alignment.MIDDLE_CENTER,
                        fill='favour',
                    )]
                ),

                RectElement(
                    size=CARD_SIZE,
                    fill='darker_favour',
                    alignment=Alignment.MIDDLE_CENTER,
                    children=[TextElement(
                        text='ARENA',
                        font_path='alegreya_bold',
                        font_size=50,
                        alignment=Alignment.MIDDLE_CENTER,
                        fill='favour',
                    )]
                ),
            ]]
        ),

        
    ],
)

src = ManualSource([{}])
schema.process(src)
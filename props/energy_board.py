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
    dimensions=Point(CARD_WIDTH // 2 * 7, int(CARD_HEIGHT // 3)),
    naming='EnergyBoard',
    deck_name='crowd',
    background='energy',
    elements=[
        GridElement(
            grid=[[
                EllipseElement(
                    size=Point(80, 80),
                    alignment=Alignment.MIDDLE_CENTER,
                    offset=Point(PARENT / 10 * i, -7),
                    fill='dark_energy',
                    children=[
                        TextElement(
                            text=f'{i - 2}',
                            alignment=Alignment.MIDDLE_CENTER,
                            font_path='alegreya',
                            font_size=50,
                            offset=Point(0, -16),
                            fill='energy',
                        )
                    ],
                )
                for i in range(9)
            ]],
            size=Point(PARENT - 100, 100),
            offset=Point(12, 10),
        ),        
    ],
)

src = ManualSource([{}])
schema.process(src)
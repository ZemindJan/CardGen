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
from elements.grid import GridElement
from elements.group import GroupElement
from core.icon import Icon

Icon(
    name='Energy',
    path='Energy.png',
    transparent=True,
    size=Point(20, 20),
    offset=Point(0, 5)
)

Settings.CardsDirectory = 'out/props/4.2'

CARD_HEIGHT = int(3.5 * 96 * 2) // 2
CARD_WIDTH = int(2.5 * 96 * 2) // 2
CARD_SIZE = Point(CARD_WIDTH, CARD_HEIGHT)

SLOTS = 7

schema = Schema(
    dimensions=Point(CARD_WIDTH, CARD_HEIGHT * 4),
    naming='TurnsBoard',
    deck_name='crowd',
    background='energy',
    elements=[
        GridElement(
            [[
                RectElement(size=Point(PARENT, PARENT), visible=False,),
                RectElement(size=Point(PARENT, PARENT), fill='favour'),
                RectElement(size=Point(PARENT, PARENT), fill='champ_red'),
                RectElement(size=Point(PARENT, PARENT), fill='champ_blue')
            ]]
        ),

        GridElement(
            
            [

                [
                    TextElement(
                        text=f'Round',
                        font_path='alegreya_bold',
                        font_size=15,
                        fill='black',
                        alignment=Alignment.MIDDLE_CENTER
                    ), 
                    TextElement(
                        text=f'Crowd',
                        font_path='alegreya_bold',
                        font_size=15,
                        fill='black',
                        alignment=Alignment.MIDDLE_CENTER
                    ), 
                    TextElement(
                        text=f'P1',
                        font_path='alegreya_bold',
                        font_size=15,
                        fill='black',
                        alignment=Alignment.MIDDLE_CENTER
                    ), 
                    TextElement(
                        text=f'P2',
                        font_path='alegreya_bold',
                        font_size=15,
                        fill='black',
                        alignment=Alignment.MIDDLE_CENTER
                    ), 
                ],
                *[[
                    TextElement(
                        text=f'{i + 1}',
                        font_path='alegreya',
                        font_size=30,
                        fill='black',
                        alignment=Alignment.MIDDLE_LEFT,
                        offset=Point(10, 0),
                    ), 
                    TextElement(
                        text=f'+' if i % 3 == 0 else '',
                        font_path='alegreya',
                        font_size=30,
                        fill='black',
                        alignment=Alignment.MIDDLE_CENTER
                    ),
                    TextElement(
                        text=f'#Energy' if i % 2 == 0 else 'draw',
                        font_path='alegreya',
                        font_size=15,
                        fill='white',
                        alignment=Alignment.MIDDLE_CENTER
                    ),
                    TextElement(
                        text=f'#Energy' if i % 2 == 1 else 'draw',
                        font_path='alegreya',
                        font_size=15,
                        fill='white',
                        alignment=Alignment.MIDDLE_CENTER
                    ), 
                ] for i in range(24)]
            ]
        )
    ]
)

src = ManualSource([{}])
schema.process(src)
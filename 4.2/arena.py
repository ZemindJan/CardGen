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

Settings.CardsDirectory = 'out/cards/4.2'
Settings.DecksDirectory = 'out/decks/4.2'

URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=531382424&single=true&output=csv'

CARD_HEIGHT = int(3.5 * 96 * 2)
CARD_WIDTH  = int(2.5 * 96 * 2)

schema = Schema(
    dimensions=Point(CARD_WIDTH, CARD_HEIGHT),
    naming='$blessings$',
    deck_name='arena',
    required_entry_fields=['blessings', 'effect'],
    background='darker_favour',
    elements=[
        RectElement(
            size=Point(PARENT - 2 * 20, PARENT / 5),
            offset=Point(20, 0),
            visible=False,
            children=[
                TextElement(
                    text='The Gods bless you with..',
                    font_path='alegreya_italic',
                    fill='white',
                    font_size=50,
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),

        RectElement(
            size=Point(PARENT - 2 * 20, PARENT / 5),
            offset=Point(20, PARENT / 5 - 30),
            visible=False,
            children=[
                TextElement(
                    text='$blessings$',
                    font_path='alegreya_bold',
                    fill='favour',
                    font_size=100,
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),

        RectElement(
            size=Point(PARENT - 2 * 20, PARENT * 3 / 5),
            offset=Point(20, PARENT * 2 / 5 - 30),
            visible=False,
            children=[
                TextElement(
                    text='$effect$',
                    font_path='alegreya',
                    fill='white',
                    font_size=60,
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),
    ],
    back_elements=[
        RectElement(
            size=Point(PARENT, PARENT),
            fill='darker_favour',
            children=[
                TextElement(
                    text='ARENA',
                    font_path='alegreya_bold',
                    fill='favour',
                    font_size=200,
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),
    ]
)

src = OnlineSource(url=URL)
src.preprocessors.append(preprocess_fields(['desire']))
schema.process(src)
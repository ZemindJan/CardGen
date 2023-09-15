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

URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=1141313585&single=true&output=csv'

CARD_HEIGHT = int(3.5 * 96 * 2)
CARD_WIDTH = int(2.5 * 96 * 2)

schema = Schema(
    dimensions=Point(CARD_WIDTH, CARD_HEIGHT),
    naming='$name$',
    deck_name='crowd',
    required_entry_fields=['name', 'desire'],
    elements=[
        RectElement(
            size=Point(PARENT - 2 * 20, PARENT / 5),
            offset=Point(20, 0),
            visible=False,
            children=[
                TextElement(
                    text='The crowd wants to see..',
                    font_path='alegreya_italic',
                    fill='muted_blue',
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
                    text='$name$',
                    font_path='alegreya_bold',
                    fill='black',
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
                    text='$desire$',
                    font_path='alegreya',
                    fill='black',
                    font_size=60,
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),
    ],
    back_elements=[
        RectElement(
            size=Point(PARENT, PARENT),
            fill='white',
            children=[
                TextElement(
                    text='CROWD',
                    font_path='alegreya_bold',
                    fill='black',
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
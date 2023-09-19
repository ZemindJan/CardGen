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


url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=559014483&single=true&output=csv'


Settings.CardsDirectory = 'out/cards/4.2/backs'

CARD_HEIGHT = int(4.75 * 96 * 2)
CARD_WIDTH = int(2.75 * 96 * 2)

schema = Schema(
    dimensions=Point(CARD_WIDTH, CARD_HEIGHT),
    naming='$deck$',
    deck_name='4.2',
    group_by='$deck$',
    required_entry_fields=['deck'],
    elements=[
        RectElement(
            fill='white',
            offset=Point(0, 0),
            size=Point(PARENT, PARENT),
            outline=Outline(
                color='gold',
                width=20,
            ),
            children=[
                TextElement(
                    text='$deck$',
                    font_path='alegreya_bold',
                    fill='gold',
                    font_size=120,
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),
    ],
)

online_src = OnlineSource(url)

# choose source
src = online_src

# only process if run directly
if __name__ == "__main__":
    schema.process(src)
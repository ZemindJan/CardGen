from cardsmith import *
from data.source import OnlineSource
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from elements.image import ImageElement
from settings import Settings

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=2107122856&single=true&output=csv'


Settings.CardsDirectory = 'out/cards/4.0'
Settings.DecksDirectory = 'out/decks/4.0'

schema = Schema(
    dimensions=Point(2.5 * 96 * 2, 3.5 * 96 * 2),
    naming='$name$',
    deck_name='3.9 ',
    group_by='$deck$',
    required_entry_fields=['name', 'initiative', 'suite', 'combo', 'effect'],
    elements=[
        
    ],
    back_elements=[

    ]
)

schema.process(OnlineSource(url))
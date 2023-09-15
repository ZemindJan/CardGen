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

Settings.CardsDirectory = 'out/props/4.2'

CARD_HEIGHT = int(3.5 * 96 * 2) // 2
CARD_WIDTH = int(2.5 * 96 * 2) // 2
CARD_SIZE = Point(CARD_WIDTH, CARD_HEIGHT)

SLOTS = 7

def card_group(is_opp = False):
    return GroupElement(
        size=Point(PARENT, PARENT),
        children=[
            RectElement(
                size=Point(PARENT, PARENT / 2),
                fill= 'champ_blue' if is_opp else 'champ_red',
            ),
            MirrorElement(
                size=CARD_SIZE,
                offset=Point(PARENT - CARD_SIZE.x - 100, 100),
                children=[
                    RectElement(
                        size=Point(PARENT, PARENT),
                        fill= 'card_blue' if is_opp else 'card_red',
                        children=[TextElement(
                            text='DECK' if is_opp else 'DISCARD',
                            font_path='alegreya_bold',
                            fill='champ_blue' if is_opp else 'champ_red',
                            font_size=50,
                            alignment=Alignment.MIDDLE_CENTER,
                        )]
                    )
                ]
            ),
            MirrorElement(
                size=CARD_SIZE,
                offset=Point(100, 100),
                children=[
                    RectElement(
                        size=Point(PARENT, PARENT),
                        fill= 'card_blue' if is_opp else 'card_red',
                        children=[TextElement(
                            text='DECK' if not is_opp else 'DISCARD',
                            font_path='alegreya_bold',
                            fill='champ_blue' if is_opp else 'champ_red',
                            font_size=50,
                            alignment=Alignment.MIDDLE_CENTER,
                        )]
                    )
                ]
            ),
        ] + [
            RectElement(
                size=CARD_SIZE,
                offset=Point(PARENT * (1/3 * 1/2 + 2/3 * (ratio := (i / (SLOTS) + 1 / ((SLOTS) * (SLOTS + 1))))), 500),
                fill='card_blue' if is_opp else 'card_red'
            ) for i in range(SLOTS)
        ]
    )

schema = Schema(
    dimensions=Point(CARD_WIDTH * 12, CARD_HEIGHT * 6),
    naming='FavourBoard',
    deck_name='crowd',
    elements=[
        MirrorElement(
            size=Point(PARENT, PARENT), 
            children=[card_group(True)]
        ),

        GroupElement(
            size=Point(PARENT, PARENT),
            children=[card_group()],
        ),
    ]
)

src = ManualSource([{}])
schema.process(src)
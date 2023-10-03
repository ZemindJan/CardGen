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


Settings.CardsDirectory = 'out/cards/4.2'
Settings.DecksDirectory = 'out/decks/4.2'

BLACK_OUTLINE_WIDTH = 2
SIDE_COLUMN_RATIO = 1/20
GOLD_OUTLINE_WIDTH = 8
EFFECT_X_BUFFER = 3 
CARD_HEIGHT = int(4.75 * 96 * 2)
CARD_WIDTH = int(2.75 * 96 * 2)

COMBO_BANNER_SIZE = Point(100, 50)
TEXT_REPLACEMENTS = {
    '\n' : '<br>',
    'dmg' : '#Damage',
    'blk' : '#Block',
}
SUIT_COLORS = {
    'High' : 'muted_green',
    'Middle' : 'muted_yellow',
    'Low' : 'muted_red',
    'Skill' : 'grey',
    'Multi' : 'purple',
}

combos = GroupElement(
    size=Point(PARENT, PARENT),
    children=[
        # COMBOS
        ConditionalElement(condition='$cl$=X', on_true=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(PARENT - COMBO_BANNER_SIZE.x, 160 + (COMBO_BANNER_SIZE.y + 5) * 2),
                fill='red',
                children=[
                    TextElement(
                        text='LOW',
                        fill='black',
                        font_size=28,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),
        
        ConditionalElement(condition='$cm$=X', on_true=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(PARENT - COMBO_BANNER_SIZE.x, 160 + (COMBO_BANNER_SIZE.y + 5) * 1),
                fill='yellow',
                children=[
                    TextElement(
                        text='MID',
                        fill='black',
                        font_size=28,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),
        
        ConditionalElement(condition='$ch$=X', on_true=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(PARENT - COMBO_BANNER_SIZE.x, 160 + (COMBO_BANNER_SIZE.y + 5) * 0),
                fill='green',
                children=[
                    TextElement(
                        text='HIGH',
                        fill='black',
                        font_size=28,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),

        # POSITIONS
        ConditionalElement(condition='$low$=X', on_true=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(1, 160 + (COMBO_BANNER_SIZE.y + 5) * 2),
                fill='red',
                children=[
                    TextElement(
                        text='LOW',
                        fill='black',
                        font_size=28,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),
        
        ConditionalElement(condition='$mid$=X', on_true=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(1, 160 + (COMBO_BANNER_SIZE.y + 5) * 1),
                fill='yellow',
                children=[
                    TextElement(
                        text='MID',
                        fill='black',
                        font_size=28,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),
        
        ConditionalElement(condition='$high$=X', on_true=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(1, 160 + (COMBO_BANNER_SIZE.y + 5) * 0),
                fill='green',
                children=[
                    TextElement(
                        text='HIGH',
                        fill='black',
                        font_size=28,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),
    ]
)

a_side = GroupElement(
    size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT / 2 - BLACK_OUTLINE_WIDTH),
    offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
    children=[
        # Background
        RectElement(
            offset=Point(1, 1),
            size=Point(PARENT - BLACK_OUTLINE_WIDTH, PARENT  - BLACK_OUTLINE_WIDTH)
        ).on_draw_set_fields(fill=f'$lookup suit {SUIT_COLORS}$'),

        # Title
        RectElement(
            size=Point(PARENT - 120, 60),
            offset=Point(20, 20),
            visible=False,
            children=[
                TextElement(
                    text='$aname$',
                    fill='black',
                    font_size=60,
                    font_path='alegreya_bold',
                    alignment=Alignment.MIDDLE_CENTER
                )
            ],
        ),

        # Traits
        RectElement(
            size=Point(PARENT, 40),
            offset=Point(0, 100),
            visible=False,
            children=[
                TextElement(
                    text='$atraits$',
                    fill='black',
                    font_size=40,
                    font_path='alegreya_italic',
                    alignment=Alignment.MIDDLE_CENTER
                )
            ],
        ),

        # Cost
        EllipseElement(
            size=Point(80, 80),
            offset=Point(-20, 20),
            alignment=Alignment.TOP_RIGHT,
            fill='energy',
            outline=Outline(
                color='dark_energy',
                width=5,
            ),
            children=[
                TextElement(
                    text='$acost$',
                    fill='black',
                    font_size=60,
                    font_path='alegreya_bold',
                    alignment=Alignment.MIDDLE_CENTER,
                    offset=Point(0, -17),
                )
            ]
        ),

        # Effect
        RectElement(
            size=Point(PARENT - COMBO_BANNER_SIZE.x * 2 - 10, PARENT - 180),
            offset=Point(COMBO_BANNER_SIZE.x + 5, 160),
            visible=False,
            children=[
                TextElement(
                    text='$aeffect$',
                    fill='black',
                    font_size=35,
                    font_path='alegreya',
                    alignment=Alignment.MIDDLE_CENTER,
                    line_alignment=YAlignment.MIDDLE,
                )
            ]
        ),

        combos
    ]
)

d_side = GroupElement(
    size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT / 2 - BLACK_OUTLINE_WIDTH),
    offset=Point(BLACK_OUTLINE_WIDTH, PARENT / 2),
    children=[
        RectElement(
            fill='muted_blue',
            size=Point(PARENT, PARENT)
        ),

        # Title
        RectElement(
            size=Point(PARENT - 120, 60),
            offset=Point(20, 20),
            visible=False,
            children=[
                TextElement(
                    text='$dname$',
                    fill='black',
                    font_size=60,
                    font_path='alegreya_bold',
                    alignment=Alignment.MIDDLE_CENTER
                )
            ],
        ),

        # Traits
        RectElement(
            size=Point(PARENT, 40),
            offset=Point(0, 100),
            visible=False,
            children=[
                TextElement(
                    text='$dtraits$',
                    fill='black',
                    font_size=40,
                    font_path='alegreya_italic',
                    alignment=Alignment.MIDDLE_CENTER
                )
            ],
        ),
        
        # Cost
        EllipseElement(
            size=Point(80, 80),
            offset=Point(-20, 20),
            alignment=Alignment.TOP_RIGHT,
            fill='energy',
            outline=Outline(
                color='dark_energy',
                width=5,
            ),
            children=[
                TextElement(
                    text='$dcost$',
                    fill='black',
                    font_size=60,
                    font_path='alegreya_bold',
                    alignment=Alignment.MIDDLE_CENTER,
                    offset=Point(0, -17),
                )
            ]
        ),

        # Effect
        RectElement(
            size=Point(PARENT - COMBO_BANNER_SIZE.x * 2 - 10, PARENT - 180),
            offset=Point(COMBO_BANNER_SIZE.x + 5, 160),
            visible=False,
            children=[
                TextElement(
                    text='$deffect$',
                    fill='black',
                    font_size=35,
                    font_path='alegreya',
                    alignment=Alignment.MIDDLE_CENTER,
                    line_alignment=YAlignment.MIDDLE,
                )
            ]
        ),
    ]
)

schema = Schema(
    dimensions=Point(CARD_WIDTH, CARD_HEIGHT),
    naming='$aname$ $dname$ $index$',
    text_replacements=TEXT_REPLACEMENTS,
    deck_name='4.2',
    group_by='$deck$',
    count='$copies$',
    required_entry_fields=['aname', 'copies', 'low', 'mid', 'high', 'suit', 'atraits', 'acost', 'aeffect', 'cl', 'cm', 'ch', 'dname', 'dcost', 'dtraits', 'deffect', 'deck'],
    elements=[
        # Black Border
        RectElement(
            fill='black',
            offset=Point(0, 0),
            size=Point(PARENT, PARENT),
        ),

        a_side,
        d_side,
    ],
    back_elements=[
        TextElement(
            text='CARD',
            font_path='alegreya_bold',
            fill='black',
            font_size=100,
            alignment=Alignment.MIDDLE_CENTER,
        )
    ]
)

manual_src = ManualSource(entries=[{
    'aname' : 'Flying Kick',
    'copies' : '2',
    'low' : '-',
    'mid' : 'X',
    'high': 'X',
    'suit' : 'High',
    'atraits' : 'Air, Kick',
    'acost' : '2',
    'aeffect' : 'Launch Self<br>5 #Damage',
    'cl' : 'X',
    'cm' : 'X',
    'ch' : '-',
    'dname' : 'Quick Leap',
    'dcost' : '1',
    'dtraits' : 'Air, Move',
    'deffect' : 'Dodge Low<br>Launch Self',
    'deck' : 'Test'
}])

online_src = OnlineSource(url)

# choose source
src = online_src
src.preprocessors.append(
    preprocess_fields(['aeffect', 'deffect']),
)

# only process if run directly
if __name__ == "__main__":
    schema.process(src)
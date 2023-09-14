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

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=559014483&single=true&output=csv'


Settings.CardsDirectory = 'out/cards/4.2'
Settings.DecksDirectory = 'out/decks/4.2'

BLACK_OUTLINE_WIDTH = 2
SIDE_COLUMN_RATIO = 1/20
GOLD_OUTLINE_WIDTH = 8
EFFECT_X_BUFFER = 3 
CARD_HEIGHT = int(3.5 * 96 * 2)
CARD_WIDTH = int(2.5 * 96 * 2)

COMBO_BANNER_SIZE = Point(70, 32)
TEXT_REPLACEMENTS = {
    '\n' : '<br>',
}
KEY_WORDS = [
    'Launch', 'Launched',
    'Ground',
    'Stun',
    'Distance',
    'Block',
    'Low', 'Middle', 'High',
    'Kick', 'Punch'
]
for key_word in KEY_WORDS:
    TEXT_REPLACEMENTS[key_word] = f'<bold>{key_word}</bold>'

schema = Schema(
    dimensions=Point(CARD_WIDTH, CARD_HEIGHT),
    naming='$aname$ $dname$ $index$',
    text_replacements=TEXT_REPLACEMENTS,
    deck_name='4.2',
    required_entry_fields=['aname', 'low', 'mid', 'high', 'suit', 'atraits', 'acost', 'aeffect', 'cl', 'cm', 'ch', 'dname', 'dcost', 'dtraits', 'deffect'],
    elements=[
        # Black Border
        RectElement(
            fill='black',
            offset=Point(0, 0),
            size=Point(PARENT, PARENT),
        ),

        # Background
        ConditionalElement('$suit$=High', [
            RectElement(
                fill='muted_green',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),
        ConditionalElement('$suit$=Middle', [
            RectElement(
                fill='muted_yellow',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),
        ConditionalElement('$suit$=Low', [
            RectElement(
                fill='muted_red',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),
        ConditionalElement('$suit$=Utility', [
            RectElement(
                fill='grey',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),

        RectElement(
            fill='muted_blue',
            offset=Point(BLACK_OUTLINE_WIDTH, int(CARD_HEIGHT*.5)),
            size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, (PARENT  - 2 * BLACK_OUTLINE_WIDTH)/2)
        ),

        ConditionalElement('$acost$=-', [], [
            RectElement(
                size=Point(70, 180),
                offset=Point(390, 0),
                visible=False,
                children=[
                    TextElement(
                        text='$acost$',
                        fill='black',
                        font_size=80,
                        font_path='alegreya_bold'
                    )
                ]
        )]),

        # A Cost
        ConditionalElement('$acost$=-', on_true=[
            RectElement(
                size=Point(PARENT - 120, 60),
                offset=Point(60, 20),
                visible=False,
                children=[
                    TextElement(
                        text='$aname$',
                        fill='black',
                        font_size=60,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ])
        ], on_false=[
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
        )]),

        # A Effect
        RectElement(
            size=Point(PARENT - COMBO_BANNER_SIZE.x * 2 - 10, 300),
            offset=Point(COMBO_BANNER_SIZE.x + 5, 60),
            visible=False,
            children=[
                TextElement(
                    text='$aeffect$',
                    fill='black',
                    font_size=35,
                    font_path='alegreya',
                    alignment=Alignment.MIDDLE_CENTER
                )
            ]
        ),

        # COMBOS
        ConditionalElement(condition='$cl$=X', on_true=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(PARENT - COMBO_BANNER_SIZE.x, 240),
                fill='red',
                children=[
                    TextElement(
                        text='LOW',
                        fill='black',
                        font_size=18,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]).else_if(condition='$cm$=X', elements=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(PARENT - COMBO_BANNER_SIZE.x, 200),
                fill='yellow',
                children=[
                    TextElement(
                        text='MID',
                        fill='black',
                        font_size=18,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]).else_if(condition='$ch$=X', elements=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(PARENT - COMBO_BANNER_SIZE.x, 160),
                fill='green',
                children=[
                    TextElement(
                        text='HIGH',
                        fill='black',
                        font_size=18,
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
                offset=Point(0, 240),
                fill='red',
                children=[
                    TextElement(
                        text='LOW',
                        fill='black',
                        font_size=18,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]).else_if(condition='$mid$=X', elements=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(0, 200),
                fill='yellow',
                children=[
                    TextElement(
                        text='MID',
                        fill='black',
                        font_size=18,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]).else_if(condition='$high$=X', elements=[
            RectElement(
                size=COMBO_BANNER_SIZE,
                offset=Point(0, 160),
                fill='green',
                children=[
                    TextElement(
                        text='HIGH',
                        fill='black',
                        font_size=18,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ])
    ],
    back_elements=[

    ]
)


manual_src = ManualSource(entries=[
    {
        'aname' : 'discombobulate',
        'low' : '-',
        'mid' : '-',
        'high' : '-',
        'suit' : 'Utility',
        'atraits' : 'kick',
        'acost' : '2',
        'aeffect' : 'testing a really long line',
        'cl' : '-',
        'cm' : '-',
        'ch' : '-',
        'dname' : 'dicombobulate',
        'dcost' : '-',
        'dtraits' : 'kick',
        'deffect' : 'effect',
    }
])

schema.process(OnlineSource(url))
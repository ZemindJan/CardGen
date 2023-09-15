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
    'Launched', 'Launch',
    'Grounded', 'Ground',
    'Stun',
    'Distance',
    'Block',
    'Low', 'Middle', 'High',
    'Kick', 'Punch',
    'Drike', 'Imbibe',
    'Combo',
    'Momentum',
    'Cascade',
]
MALFORMED_KEY_WORDS = {
    '<bold><bold>Ground</bold>ed</bold>' : '<bold>Grounded</bold>',
    '<bold><bold>Launch</bold>ed</bold>' : '<bold>Launched</bold>'
}
SUIT_COLORS = {
    'High' : 'muted_green',
    'Middle' : 'muted_yellow',
    'Low' : 'muted_red',
    'Utility' : 'grey',
    'Multi' : 'purple',
}

def preprocess(entry : dict[str, str]) -> dict[str, str]:
    for key_word in KEY_WORDS:
        bolded_key_word = f'<bold>{key_word}</bold>'

        entry['aeffect'] = entry['aeffect'].replace(key_word, bolded_key_word)  
        entry['deffect'] = entry['deffect'].replace(key_word, bolded_key_word)

    for malformed, correct in MALFORMED_KEY_WORDS.items():
        entry['aeffect'] = entry['aeffect'].replace(malformed, correct)  
        entry['deffect'] = entry['deffect'].replace(malformed, correct)

    return entry

schema = Schema(
    dimensions=Point(CARD_WIDTH, CARD_HEIGHT),
    naming='$aname$ $dname$ $index$',
    text_replacements=TEXT_REPLACEMENTS,
    deck_name='4.2',
    group_by='$deck$',
    required_entry_fields=['aname', 'low', 'mid', 'high', 'suit', 'atraits', 'acost', 'aeffect', 'cl', 'cm', 'ch', 'dname', 'dcost', 'dtraits', 'deffect'],
    elements=[
        # Black Border
        RectElement(
            fill='black',
            offset=Point(0, 0),
            size=Point(PARENT, PARENT),
        ),

        # Background
        RectElement(
            offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
            size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
        ).on_draw_set_fields(fill=f'$lookup suit {SUIT_COLORS}$'),

        # A Cost
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

        # A Title
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
        ]),
        
        ConditionalElement(condition='$cm$=X', on_true=[
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
        ]),
        
        ConditionalElement(condition='$ch$=X', on_true=[
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
        ]),
        
        ConditionalElement(condition='$mid$=X', on_true=[
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
        ]),
        
        ConditionalElement(condition='$high$=X', on_true=[
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
        ]),

        MirrorElement(size=Point(PARENT, PARENT), offset=Point(0, PARENT / 2), mirror_x=False, mirror_y=False, children=[

            RectElement(
                fill='muted_blue',
                offset=Point(BLACK_OUTLINE_WIDTH, 0),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, (PARENT  - 1 * BLACK_OUTLINE_WIDTH))
            ),

            # A Cost
            ConditionalElement('$dcost$=-', [], [
                RectElement(
                    size=Point(70, 180),
                    offset=Point(390, 0),
                    visible=False,
                    children=[
                        TextElement(
                            text='$dcost$',
                            fill='black',
                            font_size=80,
                            font_path='alegreya_bold'
                        )
                    ]
            )]),

            # A Title
            ConditionalElement('$dcost$=-', on_true=[
                RectElement(
                    size=Point(PARENT - 120, 60),
                    offset=Point(60, 20),
                    visible=False,
                    children=[
                        TextElement(
                            text='$dname$',
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
                            text='$dname$',
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
                        text='$deffect$',
                        fill='black',
                        font_size=35,
                        font_path='alegreya',
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

online_src = OnlineSource(url)

# choose source
src = online_src
src.preprocessors.append(preprocess)
schema.process(src)
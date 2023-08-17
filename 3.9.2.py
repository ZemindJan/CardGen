from cardsmith import *
from data.source import OnlineSource
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from elements.image import ImageElement
from settings import Settings

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=694111189&single=true&output=csv'

BLACK_OUTLINE_WIDTH = 2
SIDE_COLUMN_RATIO = 1/20
GOLD_OUTLINE_WIDTH = 8
EFFECT_X_BUFFER = 3

SUITE_SIZE = Point(180, 180)

KEYWORDS = ['Guarantee', 'On Reveal', 'Contract', 'Violation', 'Recover', 'Replace', 'Stamina']
REPLACEMENTS = {}

for KEYWORD in KEYWORDS:
    REPLACEMENTS[f'{KEYWORD}'] = f'<bold>{KEYWORD}</bold>'
    REPLACEMENTS[f'<bold>{KEYWORD}</bold>:'] = f'<bold>{KEYWORD}:</bold><br>'

Settings.CardsDirectory = 'out/cards/3.9.2'
Settings.DecksDirectory = 'out/decks/3.9.2'

schema = Schema(
    dimensions=Point(750, 1050),
    naming='$name$',
    deck_name='3.9.2 ',
    group_by='$deck$',
    count='$copies$',
    required_entry_fields=['name', 'type', 'effect', 'deck', 'cost'],
    text_replacements=REPLACEMENTS,
    elements=[
        # Black Border
        RectElement(
            fill='black',
            offset=Point(0, 0),
            size=Point(PARENT, PARENT),
            #outline='gold',
            #outlineWidth=8,
        ),

        # Background
        ConditionalElement('$type$=Blades', [
            RectElement(
                fill='muted_green',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),
        ConditionalElement('$type$=Stone', [
            RectElement(
                fill='muted_red',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),
        ConditionalElement('$type$=Scrolls', [
            RectElement(
                fill='muted_blue',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),
        ConditionalElement('$type$=Blank', [
            RectElement(
                fill='white',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),

        # Text
        RectElement(
            fill='white',
            offset=Point(PARENT * SIDE_COLUMN_RATIO, PARENT * (1/5)),
            size=Point(PARENT * (1 - 1 / 10), PARENT * (1 - 1 / 5 - SIDE_COLUMN_RATIO)),
            outline='gold',
            outlineWidth=GOLD_OUTLINE_WIDTH,
        ),

        RectElement(
            fill='white',
            offset=Point(PARENT * SIDE_COLUMN_RATIO + GOLD_OUTLINE_WIDTH, PARENT * (1/5) + GOLD_OUTLINE_WIDTH),
            size=Point(PARENT * (1 - 1 / 10) - 2 * GOLD_OUTLINE_WIDTH, PARENT * (1 - 1 / 5 - SIDE_COLUMN_RATIO) - 2 * GOLD_OUTLINE_WIDTH),
            children=[
                RectElement(
                    fill='white',
                    offset=Point(EFFECT_X_BUFFER, 0),
                    size=Point(PARENT - 2 * EFFECT_X_BUFFER, PARENT),
                    children=[
                        TextElement(
                            text='$effect$',
                            font_path='alegreya',
                            fill='black',
                            font_size=60,
                            alignment=MiddleCenter,
                            max_icon_size=Point(70, 70),
                        )
                    ],
                ).make_invisible(),
            ],
        ),
                    
        # Title
        RectElement(
            fill='blank',
            offset=Point(PARENT * SIDE_COLUMN_RATIO, 50),
            size=Point(PARENT * (1 - SIDE_COLUMN_RATIO) - SUITE_SIZE.x, 80),
            alignment=TopLeft,
            children=[
                TextElement(
                    text='$name$',
                    font_path='alegreya_bold',
                    fill='black',
                    font_size=130,
                    alignment=MiddleLeft,
                    offset=Point(0, -10),
                ),
            ]
        ).make_invisible(),

        # Subtitle
        ConditionalElement('god?', [
            RectElement(
                fill='blank',
                offset=Point(PARENT * SIDE_COLUMN_RATIO, 160),
                size=Point(PARENT * (1 - SIDE_COLUMN_RATIO) - SUITE_SIZE.x, 40),
                alignment=TopLeft,
                children=[
                    TextElement(
                        text='$god$',
                        font_path='alegreya_italic',
                        fill='black',
                        font_size=72,
                        alignment=MiddleLeft,
                        offset=Point(0, -15),
                    ),
                ]
            ).make_invisible(),
        ]),

        # Suites
        ConditionalElement('$type$=Blades', [
            ImageElement(
                offset=Point(-10, 10),
                name='Blades Suite.png',
                alignment=TopRight,
                size=SUITE_SIZE,
            )
        ]),
        ConditionalElement('$type$=Stone', [
            ImageElement(
                offset=Point(-10, 10),
                name='Stone Suite.png',
                alignment=TopRight,
                size=SUITE_SIZE,
            )
        ]),
        ConditionalElement('$type$=Scrolls', [
            ImageElement(
                offset=Point(-10, 10),
                name='Scrolls Suite.png',
                alignment=TopRight,
                size=SUITE_SIZE,
            )
        ]),
        ConditionalElement('$type$=Null', [
            ImageElement(
                offset=Point(-10, 10),
                name='Load Field.png',
                alignment=TopRight,
                size=SUITE_SIZE,
            )
        ]),

        #Load
        ImageElement(
            offset=Point(-10, 200),
            name='Load Field.png',
            alignment=TopRight,
            size=Point(100, 100),
            children=[
                TextElement(
                    text='$cost$',
                    font_path='alegreya_italic',
                    fill='black',
                    font_size=72,
                    alignment=MiddleCenter,
                ),
        ]),

        RectElement(
            fill='blank',
            offset=Point(-10, 200),
            size=Point(100, 100),
            alignment=TopRight,
            children=[
                TextElement(
                    text='Load',
                    font_path='alegreya_bold',
                    fill='black',
                    font_size=20,
                    alignment=MiddleCenter,
                    offset=Point(0, -30),
                ),                
                TextElement(
                    text='$cost$',
                    font_path='alegreya_bold',
                    fill='black',
                    font_size=80,
                    alignment=MiddleCenter,
                    offset=Point(0, -15),
                ),
            ]
        ).make_invisible()     
    ],
    back_elements=[
        RectElement(
            fill='gold',
            offset=Point(0, 0),
            size=Point(PARENT, PARENT),
            outline='black',
            outlineWidth=BLACK_OUTLINE_WIDTH,
        ),

        RectElement(
            fill='gold',
            outline='white',
            outlineWidth=20,
            offset=Point(50, 50),
            size=Point(PARENT - 100, PARENT - 100),
        ),

        RectElement(
            fill='gold',
            offset=Point(70, 70),
            size=Point(PARENT - 140, PARENT - 440),
            children=[
                TextElement(
                    text='GOD',
                    fill='white',
                    font_path='alegreya_bold',
                    font_size=200,
                    alignment=MiddleCenter
                )
            ]
        )
    ]
)

schema.process(OnlineSource(url))
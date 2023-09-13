from cardsmith import *
from data.source import OnlineSource
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from elements.image import ImageElement
from settings import Settings
from elements.shape import Outline

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=2107122856&single=true&output=csv'


Settings.CardsDirectory = 'out/cards/4.0'
Settings.DecksDirectory = 'out/decks/4.0'

BLACK_OUTLINE_WIDTH = 2
SIDE_COLUMN_RATIO = 1/20
GOLD_OUTLINE_WIDTH = 8
EFFECT_X_BUFFER = 3

schema = Schema(
    dimensions=Point(2.5 * 96 * 2, 3.5 * 96 * 2),
    naming='$name$ $index$',
    deck_name='4.0',
    required_entry_fields=['name', 'initiative', 'suite', 'effect', 'modifier'],
    elements=[
        # Black Border
        RectElement(
            fill='black',
            offset=Point(0, 0),
            size=Point(PARENT, PARENT),
        ),

        # Background
        ConditionalElement('$suite$=Spirit', [
            RectElement(
                fill='muted_green',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),
        ConditionalElement('$suite$=Body', [
            RectElement(
                fill='muted_red',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),
        ConditionalElement('$suite$=Mind', [
            RectElement(
                fill='muted_blue',
                offset=Point(BLACK_OUTLINE_WIDTH, BLACK_OUTLINE_WIDTH),
                size=Point(PARENT - 2 * BLACK_OUTLINE_WIDTH, PARENT  - 2 * BLACK_OUTLINE_WIDTH)
            )
        ]),

        RectElement(
            size=Point(70, 180),
            offset=Point(20, -20),
            visible=False,
            children=[
                TextElement(
                    text='$initiative$',
                    fill='black',
                    font_size=150,
                    font_path='alegreya_bold'
                )
            ]
        ),

        RectElement(
            size=Point(PARENT - 120, 120),
            offset=Point(100, 25),
            visible=False,
            children=[
                TextElement(
                    text='$name$',
                    fill='black',
                    font_size=80,
                    font_path='alegreya_bold',
                    alignment=Alignment.MIDDLE_CENTER
                )
            ],
        ),

        RectElement(
            size=Point(PARENT - 50, 300),
            offset=Point(25, 180),
            fill='white',
            outline=Outline(
                color='gold',
                width=8,
            ),
            children=[
                TextElement(
                    text='$effect$',
                    fill='black',
                    font_size=50,
                    font_path='alegreya',
                    alignment=Alignment.MIDDLE_CENTER
                )
            ]
        ),

        RectElement(
            size=Point(PARENT - 50, 120),
            offset=Point(25, PARENT - 210),
            visible=False,
            children=[
                TextElement(
                    text='$modifier$',
                    fill='black',
                    font_size=50,
                    font_path='alegreya_italic',
                    alignment=Alignment.MIDDLE_CENTER
                )
            ]
        ),

        ConditionalElement(condition='$cb$=X', on_true=[
            RectElement(
                size=Point(80, 80),
                offset=Point(50, PARENT - 80),
                visible=False,
                children=[
                    TextElement(
                        text='BODY',
                        fill='black',
                        font_size=50,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),

        ConditionalElement(condition='$cs$=X', on_true=[
            RectElement(
                size=Point(80, 80),
                offset=Point((PARENT - 50) / 3 + 50, PARENT - 80),
                visible=False,
                children=[
                    TextElement(
                        text='SPIRIT',
                        fill='black',
                        font_size=50,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),

        ConditionalElement(condition='$cm$=X', on_true=[
            RectElement(
                size=Point(80, 80),
                offset=Point((PARENT - 50) / 3 * 2 + 50, PARENT - 80),
                visible=False,
                children=[
                    TextElement(
                        text='MIND',
                        fill='black',
                        font_size=40,
                        font_path='alegreya_bold',
                        alignment=Alignment.MIDDLE_CENTER
                    )
                ]
            ),
        ]),

    ],
    back_elements=[

    ]
)

schema.process(OnlineSource(url))
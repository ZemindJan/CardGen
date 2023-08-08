from cardsmith import *
from data.source import OnlineSource
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from elements.image import ImageElement
from settings import Settings

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=802293359&single=true&output=csv"



SUITE_SIZE = Point(120, 120)

Settings.CardsDirectory = 'out/3.8/cards'
Settings.CardsDirectory = 'out/3.8/decks'

schema = Schema(
    naming='$name$',
    deck_name='3.8 ',
    group_by='$deck$',
    required_entry_fields=['name', 'title', 'type', 'effect', 'deck'],
    elements=[
        # Background
        ConditionalElement('$type$=Blades', [
            RectElement(
                fill='muted_green',
                offset=Point(0, 0),
                size=Point(PARENT, PARENT)
            )
        ]),
        ConditionalElement('$type$=Stone', [
            RectElement(
                fill='muted_red',
                offset=Point(0, 0),
                size=Point(PARENT, PARENT)
            )
        ]),
        ConditionalElement('$type$=Scrolls', [
            RectElement(
                fill='muted_blue',
                offset=Point(0, 0),
                size=Point(PARENT, PARENT)
            )
        ]),

        # Text
        RectElement(
            fill='white',
            offset=Point(PARENT * (1 / 20), PARENT * (1/5)),
            size=Point(PARENT * (1 - 1 / 10), PARENT * (1 - 1 / 5 - 1 / 20)),
            children=[
                TextElement(
                    text='$effect$',
                    font_path='alegreya',
                    fill='black',
                    font_size=50,
                    alignment=MiddleCenter,
                )
            ],
            outline='gold',
            outlineWidth=8,
        ),

        # Title
        RectElement(
            fill='blank',
            offset=Point(PARENT / 20, 10),
            size=Point(PARENT * (19/20) - SUITE_SIZE.x, 80),
            alignment=TopLeft,
            children=[
                TextElement(
                    text='$name$',
                    font_path='alegreya_bold',
                    fill='black',
                    font_size=55,
                    alignment=MiddleLeft,
                    offset=Point(0, -10),
                ),
            ]
        ).make_invisible(),

        # Subtitle
        RectElement(
            fill='blank',
            offset=Point(PARENT / 20, 90),
            size=Point(PARENT * (19/20) - SUITE_SIZE.x, 40),
            alignment=TopLeft,
            children=[
                TextElement(
                    text='$title$',
                    font_path='alegreya_italic',
                    fill='black',
                    font_size=36,
                    alignment=MiddleLeft,
                    offset=Point(0, -15),
                ),
            ]
        ).make_invisible(),

        # Suites
        ConditionalElement('$type$=Blades', [
            ImageElement(
                name='Blades Suite.png',
                alignment=TopRight,
                size=SUITE_SIZE,
            )
        ]),
        ConditionalElement('$type$=Stone', [
            ImageElement(
                name='Stone Suite.png',
                alignment=TopRight,
                size=SUITE_SIZE,
            )
        ]),
        ConditionalElement('$type$=Scrolls', [
            ImageElement(
                name='Scrolls Suite.png',
                alignment=TopRight,
                size=SUITE_SIZE,
            )
        ]),

        
    ],
)

schema.process(OnlineSource(url))
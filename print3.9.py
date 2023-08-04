from cardsmith import *
from data.source import OnlineSource
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from elements.image import ImageElement
from settings import Settings

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=2074238036&single=true&output=csv"



SUITE_SIZE = Point(180, 180)

schema = Schema(
    naming='$name$',
    deck_name='3.8 ',
    group_by='$deck$',
    required_entry_fields=['name', 'title', 'type', 'effect', 'deck', 'load'],
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
                offset=Point(2, 2),
                size=Point(PARENT-5, PARENT-5)
            )
        ]),
        ConditionalElement('$type$=Stone', [
            RectElement(
                fill='muted_red',
                offset=Point(2, 2),
                size=Point(PARENT-5, PARENT-5)
            )
        ]),
        ConditionalElement('$type$=Scrolls', [
            RectElement(
                fill='muted_blue',
                offset=Point(2, 2),
                size=Point(PARENT-5, PARENT-5)
            )
        ]),
        ConditionalElement('$type$=Null', [
            RectElement(
                fill='white',
                offset=Point(2, 2),
                size=Point(PARENT-5, PARENT-5)
            )
        ]),

        # Text
        RectElement(
            fill='white',
            offset=Point(PARENT * (1 / 20), PARENT * (1/5)),
            size=Point(PARENT * (1 - 1 / 10), PARENT * (1 - 1 / 5 - 1 / 20)),
            outline='gold',
            outlineWidth=8,
        ),

        RectElement(
            fill='white',
            offset=Point(PARENT * (1 / 20)+8, PARENT * (1/5)+8),
            size=Point(PARENT * (1 - 1.25 / 10), PARENT * (1 - 1 / 5 - 1 / 20) - 16),
            children=[
                TextElement(
                    text='$effect$',
                    font_path='alegreya',
                    fill='black',
                    font_size=60,
                    alignment=MiddleCenter,
                )
            ],
        ),

        # Title
        RectElement(
            fill='blank',
            offset=Point(PARENT / 20, 50),
            size=Point(PARENT * (19/20) - SUITE_SIZE.x, 80),
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
        RectElement(
            fill='blank',
            offset=Point(PARENT / 20, 160),
            size=Point(PARENT * (19/20) - SUITE_SIZE.x, 40),
            alignment=TopLeft,
            children=[
                TextElement(
                    text='$title$',
                    font_path='alegreya_italic',
                    fill='black',
                    font_size=72,
                    alignment=MiddleLeft,
                    offset=Point(0, -15),
                ),
            ]
        ).make_invisible(),

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
                    text='$load$',
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
                    text='$load$',
                    font_path='alegreya_bold',
                    fill='black',
                    font_size=80,
                    alignment=MiddleCenter,
                    offset=Point(0, -15),
                ),
            ]
        ).make_invisible(),

        

        
    ],
)

schema.process(OnlineSource(url))
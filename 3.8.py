from cardsmith import *
from data.source import OnlineSource
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from settings import Settings

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=802293359&single=true&output=csv"
Settings.IconPrefix = '!'
schema = Schema(
    naming='$name$',
    deck_name='3.8 ',
    group_by='$deck$',
    required_entry_fields=['name', 'title', 'type', 'effect', 'deck'],
    elements=[
        # Backgrounds
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

        

        # Title
        TextElement(
            text='$name$',
            font_path='alegreya_bold',
            fill='black',
            font_size=50,
            offset=Point(0, 10),
            alignment=TopCenter,
        ),

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
                    font_size=40,
                    alignment=MiddleCenter,
                )
            ]
        ),
    ],
)

schema.process(OnlineSource(url))
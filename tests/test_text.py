# Allows code to be run in root directory
import sys
import time
sys.path[0] = sys.path[0].removesuffix('\\tests')

from cardsmith import *
from elements.rect import RectElement
from elements.ellipse import EllipseElement
from elements.conditional import ConditionalElement
from elements.text import TextElement
from elements.image import ImageElement
from core.color import Black, Red
from data.source import ManualSource

schema = Schema(
    naming='test/$name$',
    elements=[
        RectElement(
            fill=Black,
            outline=Red,
            outlineWidth=2,
            offset=Point(PARENT / -6, 0),
            alignment=BottomRight,
            size=Point(PARENT / 3, 10)
        ),
        EllipseElement(
            Red, Point(-5, -5), Point(15, 15), MiddleCenter, Black, 2
        ),
        RectElement(
            fill=Red,
            offset=Point(0, 0),
            size=Point(PARENT, 100),
            children=[
                ConditionalElement(
                    condition='$name$=test',
                    on_true=[
                        TextElement(
                            text='$name$ <size=20><color=blue>is</size> <italic>the</color></italic> <bold>namep</bold>#dmg',
                            font_path='alegreya',
                            font_size=40,
                            fill=White,
                            alignment=MiddleCenter,
                        )
                    ],
                    on_false=[
                        TextElement(
                            text='$name$ <size=20><color=blue>is</size> <italic>the</color></italic> <bold>namep</bold>#dmg',
                            font_path='alegreya',
                            font_size=20,
                            fill=White,
                            alignment=MiddleCenter,
                        )
                    ]
                ),
                
            ]
        ),
        ImageElement(
            'cocktail.png',
            alignment=MiddleCenter,
            size=Point(200, 200),
        ),

        RectElement(
            fill=Red,
            alignment=BottomCenter,
            size=Point(PARENT, PARENT / 4),
            offset=Point(0, 0),
            children=[
                TextElement(
                    text='This #dmg is a test for wraps',
                    font_path='alegreya',
                    fill='white',
                    font_size=800
                )
            ]
        )
        
    ]
)

schema.process(ManualSource([
    dict(name='test'),
    dict(name='test2')
]))
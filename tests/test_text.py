# Allows code to be run in root directory
import sys
import time
sys.path[0] = sys.path[0].removesuffix('\\tests')

from cardsmith import *
from elements.rect import RectElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from core.color import Black, Red
from data.source import Local

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
                TextElement(
                    text='$name$',
                    font_path='squealer.ttf',
                    text_size=40,
                    fill=White,
                    alignment=MiddleCenter,
                )
            ]
        ),
        
    ]
)

schema.draw(dict(
    name='test'
))
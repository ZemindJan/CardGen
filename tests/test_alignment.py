# Allows code to be run in root directory
import sys
import time
sys.path[0] = sys.path[0].removesuffix('\\tests')
sys.path[0] = sys.path[0].removesuffix('/tests')

from cardsmith import *
from elements.rect import RectElement
from elements.ellipse import EllipseElement
from core.color import Colors
from data.source import LocalSource
from core.alignment import Alignment
from elements.shape import Outline

schema = Schema(
    naming='test/$name$',
    elements=[
        RectElement(
            fill=Colors.Black,
            outline=Colors.Red,
            outlineWidth=2,
            offset=Point(PARENT / -6, 0),
            alignment=Alignment.BOTTOM_RIGHT,
            size=Point(PARENT / 3, 10)
        ),
        EllipseElement(
            fill=Colors.Red, 
            offset=Point(-5, -5), 
            size=Point(15, 15), 
            alignment=Alignment.MIDDLE_CENTER, 
            outline=Outline(
                color=Colors.Black,
                outlinewidth=2,
            )
        ),
    ]
)

schema.draw_card(dict(
    name='test'
))
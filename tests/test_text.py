# Allows code to be run in root directory
import sys
import time
sys.path[0] = sys.path[0].removesuffix('\\tests')
sys.path[0] = sys.path[0].removesuffix('/tests')

from cardsmith import *
from elements.rect import RectElement
from elements.ellipse import EllipseElement
from elements.conditional import ConditionalElement
from elements.text import TextElement
from elements.image import ImageElement
from elements.polygon import PolygonElement, Outline
from core.color import Colors
from data.source import ManualSource

schema = Schema(
    naming='test/$name$',
    text_replacements={
        'test' : 'best'
    },
    count='$count$',
    elements=[
        RectElement(
            fill=Colors.White,
            outline=Outline(color=Colors.Red, width=2), 
            offset=Point(PARENT / -6, 0),
            alignment=Alignment.MIDDLE_CENTER,
            size=Point(PARENT / 3, 10)
        ),
        EllipseElement(
            fill=Colors.Red, 
            offset=Point(-5, -5), 
            size=Point(15, 15), 
            alignment=Alignment.MIDDLE_CENTER, 
            outline=Outline(color=Colors.Black, width=2), 
        ),
        RectElement(
            fill=Colors.Red,
            offset=Point(0, 0),
            size=Point(PARENT, 110),
            children=[
                ConditionalElement(
                    condition='$name$=test',
                    on_true=[
                        TextElement(
                            text='$name$ <size=50><color=blue>is</size> <italic>the</color></italic> <bold>namep</bold>#plusone',
                            font_path='alegreya',
                            font_size=200,
                            fill=Colors.White,
                            alignment=Alignment.MIDDLE_CENTER,
                            line_alignment=YAlignment.MIDDLE
                        )
                    ],
                    on_false=[
                        TextElement(
                            text='$name$ <size=80><color=blue>is</size> <italic>the</color></italic> <bold>namep</bold>#plusone',
                            font_path='alegreya',
                            font_size=200,
                            fill=Colors.White,
                            alignment=Alignment.MIDDLE_CENTER,
                            line_alignment=YAlignment.MIDDLE
                        )
                    ]
                ),
                
            ]
        ),
        ImageElement(
            'cocktail.png',
            alignment=Alignment.MIDDLE_CENTER,
            size=Point(200, 200),
        ),

        RectElement(
            fill=Colors.Red,
            alignment=Alignment.BOTTOM_CENTER,
            size=Point(PARENT, PARENT / 4),
            offset=Point(0, 0),
            children=[
                ConditionalElement(
                    condition='$name$=test',
                    on_true=[
                        TextElement(
                            text='$name$ <size=20><color=blue>is</size> <italic>the</color></italic> <bold>namep</bold>#dmg',
                            font_path='alegreya',
                            font_size=60,
                            fill=White,
                            alignment=MiddleCenter,
                        )
                    ],
                    on_false=[
                        TextElement(
                            text='$name$ <size=20><color=blue>is</size> <italic>the</color></italic> <bold>namep</bold>#dmg',
                            font_path='alegreya',
                            font_size=40,
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
                    text='This #plusone is a test for wraps',
                    font_path='alegreya',
                    fill='white',
                    font_size=800,
                    max_icon_size=Point(50, 50),
                ),
                PolygonElement(
                    fill='#00FF00',
                    points=[Point(0, 0), Point(1, 0), Point(0.5, 1)],
                    offset=Point(0, 0),
                    alignment=Alignment.MIDDLE_CENTER,
                )
            ]
        ),

        
        
    ]
)

schema.process(ManualSource([
    dict(name='test', count='2'),
    dict(name='test2', count='1')
]))
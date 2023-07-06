from cardsmith import *
from elements.rect import RectElement
from elements.ellipse import EllipseElement
from core.color import Black, Red

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
    ]
)

schema.draw(dict(
    name='test'
))
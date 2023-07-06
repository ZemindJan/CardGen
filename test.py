from cardsmith import *
from elements.rect_area import RectArea
from core.color import Black

schema = Schema(
    naming='test/$name$',
    elements=[
        RectArea(
            color=Black, 
            offset=Point(PARENT / -6, 0),
            alignment=BottomRight,
            size=Point(PARENT / 3, 10)
        )
    ]
)

schema.draw(dict(
    name='test'
))
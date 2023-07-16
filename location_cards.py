from core.schema import Schema
from data.source import OnlineSource
from elements.text import TextElement
from elements.rect import RectElement
from core.alignment import TopCenter
from core.geometry import Point

src = OnlineSource('https://docs.google.com/spreadsheets/d/e/2PACX-1vQd8e0poc7VR1-vKW3GnrVuywCL0IHOHAMfUpW3m90ctsUOgClQL04NuzVUNid8Q5Cb9PwjGT5hXPdt/pub?gid=0&single=true&output=csv')

schema = Schema(
    naming='locations/$name$',
    elements=[
        TextElement(
            text='$name$', 
            font_path='squealer', 
            fill='blue',
            font_size=40,
            offset=Point(0, 50),
            alignment=TopCenter
        )
    ]
)

schema.process(src)
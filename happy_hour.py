from core.schema import Schema
from data.source import OnlineSource, ManualSource
from elements.text import TextElement
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from core.alignment import *
from core.geometry import Point
from core.scaling import PARENT
from core.color import Color
from settings import Settings

Settings.CardsDirectory = 'out/cards/happyhour'
Settings.DecksDirectory = 'out/decks/happyhour'

src = OnlineSource('https://docs.google.com/spreadsheets/d/e/2PACX-1vTsUTYNm5FuN71tLM6uhHm4RIrSE7PhmakM-LMFUHW7ax7YAL-zMHS5mOeio5JvpRoRJUFivKnVa4X3/pub?gid=2019558398&single=true&output=csv')
schema = Schema(
    naming='card$index$',
    required_entry_fields=['name', 'ingredient', 'effect', 'icon'],
    elements=[
        RectElement(
            fill='white',
            offset=Point(0, 0),
            size=Point(PARENT, PARENT * (3/4)),
            children=[
                RectElement(
                    fill='white',
                    offset=Point(PARENT * 1/20, 50),
                    size=Point(PARENT * 9/10, 90),
                    children=[
                        TextElement(
                            text='<bold>$name$</bold>',
                            font_path='alegreya',
                            fill='black',
                            offset=Point(0, 0),
                            alignment=TopCenter,
                            font_size=60,
                        ),]
                ).make_invisible(),

                

                RectElement(
                    fill='white',
                    offset=Point(PARENT * 1/6, 70),
                    size=Point(PARENT * 2/3, PARENT - 200),
                    children=[
                        TextElement(
                            text='$effect$',
                            font_path='alegreya',
                            fill='black',
                            offset=Point(0, 100),
                            alignment=TopCenter,
                            font_size=50,
                            max_icon_size=Point(100, 100),
                        ),
                    ]
                ).make_invisible()
            ]
        ),

        RectElement(
            fill='black',
            offset=Point(0, PARENT * (1 - 1/4)),
            size=Point(PARENT, PARENT * (1/4)),
            children=[
                RectElement(
                    fill='black',
                    offset=Point(0, -10),
                    size=Point(PARENT * 4/5, PARENT),
                    children=[
                        TextElement(
                            text='$ingredient$',
                            font_path='alegreya',
                            fill='white',
                            alignment=MiddleCenter,
                            font_size=60,
                        )
                    ]
                ).make_invisible(),

                RectElement(
                    fill='black',
                    offset=Point(0, 0),
                    size=Point(PARENT - 60, PARENT),
                    children=[
                        TextElement(
                            text='$icon$',
                            font_path='alegreya',
                            fill='white',
                            alignment=MiddleRight,
                            font_size=60,
                        )
                    ]
                ).make_invisible(),
            ]
        )
    ]
)
schema.process(src)

Settings.CardsDirectory = 'out/cards/test/happyhour'
Settings.DecksDirectory = 'out/decks/test/happyhour'
schema.process(ManualSource([
    {
        'name' : 'Sazerac',
        'effect' : '#Whiskey #Aperitif #Syrup',
        'ingredient' : 'Scotch',
        'icon' : '#Whiskey #Plusone'
    }
]))
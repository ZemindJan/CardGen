from color_atlas import colors
from enum import Enum

class RGBA:
    def __init__(self, r : int, g : int, b : int, a : int = 255) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def tuple(self) -> tuple[int, int, int, int]:
        return (self.r, self.g, self.b, self.a)

Color = RGBA | str | tuple[int, int, int] | tuple[int, int, int, int]

class Colors(Enum):
    White = RGBA(255, 255, 255, 255)
    Black = RGBA(0, 0, 0, 255)
    Red = RGBA(255, 0, 0, 255)

def hexcode_to_color(hex : str) -> RGBA:
    if hex.startswith('#'):
        hex = hex[1:]

    r = int(hex[0:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)

    if len(hex) == 8:
        a = int(hex[6:8], 16)
    else:
        a = 255 

    return RGBA(r, g, b, a)

def verify_color(data : Color) -> RGBA | None:
    if isinstance(data, RGBA):
        return data
    
    if isinstance(data, Colors):
        return data.value
    
    if data is None:
        return data
    
    return make_color(data)

def make_color(data : Color) -> RGBA:
    if isinstance(data, tuple):
        return RGBA(*data)    

    if data.startswith('#'):
        return hexcode_to_color(data)
    
    if data not in colors:
        raise KeyError(f'Unknown color: {data}')
    
    return make_color(colors[data])
from color_atlas import colors

class Color:
    def __init__(self, r : int, g : int, b : int, a : int = 255) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def tuple(self) -> tuple[int, int, int, int]:
        return (self.r, self.g, self.b, self.a)

White = Color(255, 255, 255, 255)
Black = Color(0, 0, 0, 255)
Red = Color(255, 0, 0, 255)

def hexcode_to_color(hex : str) -> Color:
    if hex.startswith('#'):
        hex = hex[1:]

    r = int(hex[0:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)

    if len(hex) == 8:
        a = int(hex[6:8], 16)
    else:
        a = 255 

    return Color(r, g, b, a)

def make_color(data : str | tuple) -> Color:
    if isinstance(data, tuple):
        return Color(*data)    

    if data.startswith('#'):
        return hexcode_to_color(data)
    
    if data not in colors:
        raise KeyError(f'Unknown color: {data}')
    
    return make_color(colors[data])
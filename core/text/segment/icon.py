from core.color import RGBA, color
from core.geometry import Point
from core.text.tag import Tag
from core.text.fonts import get_font
from core.safe_paste import safe_paste
from core.text.segment.line import LineSegment
from core.alignment import YAlignment

from PIL import Image, ImageDraw, ImageFont
from core.icon import Icon, atlas
import icons
from settings import Settings

class IconSegment(LineSegment):
    icon : Icon
    
    def __init__(self, name : str, max_icon_size : Point) -> None:
        try:
            self.icon = atlas[name]
        except KeyError:
            raise ValueError(f'Icon \"{name}\" not found')

        self.image = Image.open(f'{Settings.IconsDirectory}/{self.icon.path}')
        self.name = name
        self.max_icon_size = max_icon_size

        curr_size = Point(*self.image.size)
        desired_size = self.icon.size or curr_size
         
        if max_icon_size and (desired_size.x > max_icon_size.x or desired_size.y > max_icon_size.y):
            scale_diff = max(desired_size.x / max_icon_size.x, desired_size.y / max_icon_size.y)
            desired_size = Point(desired_size.x / scale_diff, desired_size.y / scale_diff)

        # Resize if needed
        if curr_size != desired_size:
            self.image = self.image.resize(size=desired_size.int_tuple())
        
        self.size = Point(*self.image.size)

    def draw(self, coords : Point, line_size : Point, image : Image.Image, alignment : YAlignment):

        if alignment == YAlignment.TOP:
            y_offset = 0
        elif alignment == YAlignment.MIDDLE:
            y_offset = (line_size.y - self.size.y) / 2
        elif alignment == YAlignment.BOTTOM:
            y_offset =  line_size.y - self.size.y

        my_coords = coords + Point.y_span(y_offset) + self.icon.offset
        area = my_coords.to(my_coords + self.size)
        mask = self.image.copy() if self.icon.transparent else None 
        safe_paste(canvas=image, image=self.image, area=area, transparency_mask=mask)
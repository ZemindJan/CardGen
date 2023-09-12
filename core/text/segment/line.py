from core.color import Color, RGBA, color
from core.geometry import Point
from core.text.tag import Tag
from core.text.fonts import get_font
from PIL import ImageDraw, ImageFont, Image
from abc import ABC, abstractmethod
from core.alignment import YAlignment

class LineSegment(ABC):
    size : Point

    @abstractmethod
    def draw(self, coords : Point, line_size : Point, image : Image.Image, alignment : YAlignment):
        pass

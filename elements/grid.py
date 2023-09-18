from PIL import Image
from core.alignment import Alignment
from core.geometry import Point, Rect
from core.schema import Schema
from core.scaling import PARENT
from elements.element import CardElement
from elements.group import GroupElement

class GridElement(GroupElement):
    def __init__(self, 
                 grid : list[list[CardElement]],  
                  offset: Point = None, 
                 alignment: Alignment = None, 
                 size: Point = None, 
                 visible: bool = True) -> 'GridElement':
        super().__init__(offset, alignment, size, [item for row in grid for item in row], visible)
        self.grid_size = Point(len(grid[0]), len(grid))
    
    def draw(self, image: Image, entry: dict[str, str], schema: Schema, parent_area: Rect, index: int = 0):
        if not self.visible:
            return
        
        area = self.calculate_area(parent_area)

        x_offset = Point.x_span(area.size().x // self.grid_size.x)
        y_offset = Point.y_span(area.size().y // self.grid_size.y)
        
        for index, child in enumerate(self.children):
            if child is None:
                continue

            x, y = index % self.grid_size.x, index // self.grid_size.x

            origin = area.p1 + x_offset * x + y_offset * y
            child_area = origin.to(origin + x_offset + y_offset)

            child.predraw(entry)
            child.draw(image, entry, schema, child_area, index)
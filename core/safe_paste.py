from PIL.Image import Image
from core.geometry import Rect, Point

def safe_paste(canvas : Image, image : Image, area : Rect, transparency_mask : Image | None = None):
    area = area.rounded()
    
    adjusted_p1 = Point(max(0, area.p1.x), max(0, area.p1.y))
    adjusted_p2 = Point(min(canvas.size[0], area.p2.x), min(canvas.size[1], area.p2.y))
    adjusted_area = Rect(adjusted_p1, adjusted_p2)

    if adjusted_p1 != area.p1 or adjusted_p2 != area.p2:
        
        diff = Rect(adjusted_p1 - area.p1, adjusted_p2 - area.p1)

        image = image.crop(diff)

        if transparency_mask:
            transparency_mask = transparency_mask.crop(area)
    
    canvas.paste(
        im = image,
        box = adjusted_area.rounded(),
        mask = transparency_mask
    )
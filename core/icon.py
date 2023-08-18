from core.geometry import Point


class Icon:
    def __init__(self, name : str, path : str, offset : Point = None, transparent : bool = True) -> None:
        self.name = name
        self.offset = offset or Point(0, 0)
        self.path = path
        self.transparent = transparent

        atlas[name] = self

atlas : dict[str, Icon] = {}
from core.geometry import Point


class Icon:
    size : Point | None

    def __init__(self, name : str, path : str, offset : Point = None, transparent : bool = True, size : Point = None) -> None:
        self.name = name
        self.offset = offset or Point(0, 0)
        self.path = path
        self.transparent = transparent
        self.size = size

        atlas[name] = self

atlas : dict[str, Icon] = {}
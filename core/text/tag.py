class Tag:
    def __init__(self, name, data : any = None) -> None:
        self.name = name
        self.data = data or []

    def opening_repr(self) -> str:
        return f'<{self.name} {self.data}>'

    def closing_repr(self) -> str:
        return f'</{self.name}>'
class Value:
    def eval(self, entry : dict[str, str]) -> str:
        pass

class StaticValue(Value):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self, entry: dict[str, str]) -> str:
        return self.value
    
class EntryValue(Value):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def eval(self, entry: dict[str, str]) -> str:
        return entry[self.name]

def parse_value(text : str) -> Value:
    text = text.strip()
    if text.startswith('$') and text.endswith('$'):
        return EntryValue(text[1:-1])
    else:
        return StaticValue(text)

class Condition:
    def eval(self, entry : dict[str, str]) -> bool:
        pass

class Equality:
    def __init__(self, value1 : Value, value2 : Value) -> None:
        self.value1 = value1
        self.value2 = value2
    
    def eval(self, entry : dict[str, str]) -> bool:
        return self.value1.eval(entry) == self.value2.eval(entry)

def parse_condition(text : str) -> Condition:
    if "=" in text:
        left, right = text.split('=')
        return Equality(parse_value(left), parse_value(right))
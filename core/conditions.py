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

class Not(Condition):
    def __init__(self, condition : Condition) -> None:
        super().__init__()
        self.condition = condition

    def eval(self, entry: dict[str, str]) -> bool:
        return not self.condition.eval(entry)

class Exists(Condition):
    def __init__(self, name : str) -> None:
        super().__init__()
        self.name = name

    def eval(self, entry: dict[str, str]) -> bool:
        return self.name in entry

class Equality(Condition):
    def __init__(self, left : Value, right : Value) -> None:
        self.left = left
        self.right = right
    
    def eval(self, entry : dict[str, str]) -> bool:
        return self.left.eval(entry) == self.right.eval(entry)
    
class And(Condition):
    def __init__(self, left : Condition, right: Condition) -> None:
        self.left = left
        self.right = right

    def eval(self, entry : dict[str, str]) -> bool:
        return self.left.eval(entry) and self.right.eval(entry)
    
class Or(Condition):
    def __init__(self, left : Condition, right: Condition) -> None:
        self.left = left
        self.right = right

    def eval(self, entry : dict[str, str]) -> bool:
        return self.left.eval(entry) or self.right.eval(entry)
    
class Boolean(Condition):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def eval(self, entry: dict[str, str]) -> bool:
        return self.value

def parse_condition(text : str) -> Condition:
    text = text.strip()

    if text.startswith('!'):
        tail = text[1:]
        return Not(condition=parse_condition(tail))

    if '|' in text:
        left, right = text.split('|')
        return Or(left=parse_condition(left), right=parse_condition(right))

    if '&' in text:
        left, right = text.split('&')
        return And(left=parse_condition(left), right=parse_condition(right))
    
    if text.endswith('?'):
        return Exists(name=text[:-1])
    
    if '!=' in text:
        left, right = text.split('!=')
        return Not(condition=Equality(left=parse_value(left), right=parse_value(right)))

    if '=' in text:
        left, right = text.split('=')
        return Equality(left=parse_value(left), right=parse_value(right))
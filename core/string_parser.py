class Tag:
    def __init__(self, name, args = None) -> None:
        self.name = name
        self.args = args or []

class StringElement:
    def __init__(self, content : str, tags : list[Tag]) -> None:
        pass

def parse_string(string : str, entry : dict[str, str], index : int = 0):
    pass

def replace_references(string : str, entry : dict[str, str], entry_index : int = 0) -> str:
    index1 = string.find('$')

    while index1 != -1:
        substring = string[index1 + 1:]
        index2 = substring.find('$')

        if index2 == -1:
            return entry
        
        index2 = index1 + index2 + 2

        before = string[:index1]
        after = string[index2:]
        name = string[index1 + 1 : index2 - 1]

        if name == 'index':
            string = before + str(entry_index) + after
        else:
            # Typical Case
            if name not in entry:
                raise ValueError(f'Variable ${name}$ not found in entry {entry}')

            string = before + entry[name] + after

        index1 = string.find('$')

    return string
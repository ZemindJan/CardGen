

def process(filename : str = 'data.csv') -> list[dict[str, str]]:
    with open(filename) as file:
        content = file.read()

    if not content:
        return []   
        
    content = clean_content(content)
    lines = content.split('\r\n')

    field_names = [name.lower() for name in split_line(lines[0])]
    data = []

    for line in lines[1:]:
        cells = split_line(line)
        entry = {}

        for i, cell in enumerate(cells):
            if i >= len(field_names):
                continue

            key = field_names[i]
            entry[key] = cell

        data.append(entry)
    
    return data

def split_line(line : str) -> list[str]:
    cells = []
    in_quotes = False
    cell = ''

    for char in line:
        if char == ',' and not in_quotes:
            cells.append(cell)
            cell = ''
        elif char == '"':
            in_quotes = not in_quotes
        else:
            cell += char

    if cell:
        cells.append(cell)

    return cells
        

def clean_content(content : str) -> str:
    content = content.replace('\\r', '\r')
    content = content.replace('\\n', '\n')
    content = content.replace("\\'", "'")

    return content

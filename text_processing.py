def split_csv_line(line : str) -> list[str]:
    parts = []
    part = ''
    in_quotes = False

    for char in line:
        if char == '\"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            parts.append(part)
            part = ''
        else:
            part += char
    
    if part != '':
        parts.append(part)

    return parts

def preprocess_effect(effect : str) -> str:
    effect = effect.replace(',', '.')
    parts = effect.split('.')
    final = ''

    for part in parts:
        final += part.strip() + '\n'

    return final

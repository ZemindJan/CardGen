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

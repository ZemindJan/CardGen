def parse_string(string : str, entry : dict[str, str], index = 0) -> str:
    index = string.find('$')

    while index != -1:
        substring = string[index + 1:]
        second_index = substring.find('$')

        if second_index == -1:
            return entry
        
        second_index = index + second_index + 2

        before = string[:index]
        after = string[second_index:]
        name = string[index + 1 : second_index - 1]

        if name == 'index':
            string = before + str(index) + after
        else:
            # Typical Case
            if name not in entry:
                raise ValueError(f'Variable ${name}$ not found in entry {entry}')

            string = before + entry[name] + after

        index = string.find('$')

    return string
from PIL import Image
from core.color import Color
from core.text.segment import TextSegment
from core.text.icon import IconSegment
from core.text.tag import Tag
from core.geometry import Point
from settings import Settings

newline = 'newline'

def parse_tag(string : str) -> Tag:
    parts = string.split(' ')
    name = parts[0]

    if len(parts) == 1:
        if '=' in name:
            name, data = name.split('=')
            return Tag(name, data)

        return Tag(name)
    elif len(parts) == 2:
        arg = parts[1]

        if '=' in arg:
            name, value = arg.split('=')
            return Tag(name, {name : value})

        return Tag(name, arg)
    elif '=' in parts[1]:
        return Tag(name, {name : value for name, value in [arg.split('=') for arg in parts[1:]]})
    else:
        return Tag(name, parts[1:])

def parse_string(string : str, font : str, font_size : int, fill : Color, max_icon_size : Point, entry : dict[str, str], index : int = 0) -> list[TextSegment]:
    string = replace_references(string, entry, index)
    
    content = ''
    tag_content = ''
    elements = []
    active_tags : list[Tag] = []
    in_tag = False
    tag_is_closing = False

    def push():
        nonlocal content
        if content != '': 
            if content.startswith(Settings.IconPrefix):
                elements.append(IconSegment(content[1:], max_icon_size))
            else:
                elements.append(TextSegment(content, font, font_size, fill, active_tags.copy()))
        content = ''

    for char in string:
        if char == '<':
            if in_tag:
                raise ValueError('You must complete a preceding tag before starting a new one')

            in_tag = True
            tag_is_closing = False
        elif char == '>':
            if not in_tag:
                raise ValueError('No matching < for closing >')

            in_tag = False

            if tag_is_closing:
                to_remove = None

                for tag in active_tags:
                    if tag.name == tag_content:
                        to_remove = tag
                        break
                
                if not to_remove:
                    raise ValueError(f'No tag to remove for </{tag_content}>')
                
                active_tags.remove(to_remove)
            else:
                if tag_content == 'br':
                    push()
                    tag_content = ''
                    elements.append(newline)
                    continue

                active_tags.append(parse_tag(tag_content))
            
            tag_content = ''

        elif char == '/' and in_tag:
            tag_is_closing = True
            push()
            
        elif char == ' ' and not in_tag:
            push()
        else:
            if in_tag:
                tag_content += char
            else:
                content += char
    
    push()

    return elements
        

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

KEY_WORDS = [
    'Launched', 'Launch',
    'Grounded', 'Ground',
    'Stun',
    'Distance',
    'Block', 'Dodge',
    'Low', 'Middle', 'High',
    'Kick', 'Punch',
    'Drink', 'Imbibe',
    'Combo',
    'Momentum', 'Cascade',
    'Favour',
    'On Hit',
    'Slow', 'Fast',

]
MALFORMED_KEY_WORDS = {
    '<bold><bold>Ground</bold>ed</bold>' : '<bold>Grounded</bold>',
    '<bold><bold>Launch</bold>ed</bold>' : '<bold>Launched</bold>'
}

def preprocess_fields(fields : list[str]):
    def preprocess(entry : dict[str, str]) -> dict[str, str]:
        for key_word in KEY_WORDS:
            bolded_key_word = f'<bold>{key_word}</bold>'

            for field in fields:
                if field in entry:
                    entry[field] = entry[field].replace(key_word, bolded_key_word)

        for malformed, correct in MALFORMED_KEY_WORDS.items():
            for field in fields:
                if field in entry:
                    entry[field] = entry[field].replace(malformed, correct)  

        return entry
    
    return preprocess
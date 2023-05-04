from text_processing import split_csv_line
from card import Card
from generate_card import generate

with open('data.csv') as f:
    data = f.read()

lines = data.split('\\r\\n')

arg_line = split_csv_line(lines[0])
cards = []

for line in lines[1:]:
    args = split_csv_line(line)
    
    while len(args) < len(arg_line):
        args.append('')

    cards.append(Card(
        Name           = args[0],
        Type           = args[1],
        BaseEffect     = args[2],
        ExtraWinEffect = args[3],
        Deck           = args[4],
    ))

for card in cards:
    generate(card)
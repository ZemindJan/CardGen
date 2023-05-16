from text_processing import split_csv_line
from card import Card
from generate_card import generate_card, generate_back, generate_deck

with open('data.csv') as f:
    data = f.read()

lines = data.split('\\r\\n')

arg_line = split_csv_line(lines[0])
cards : list[Card] = []

for line in lines[1:]:
    args = split_csv_line(line)
    
    while len(args) < len(arg_line):
        args.append('')

    if args[0] == '': # skip empty lines
        continue

    cards.append(Card(
        Name           = args[0],
        Title          = args[1],
        Type           = args[2],
        Effect         = args[3],
        Deck           = args[4],
    ))

decks = {}

for card in cards:
    generate_card(card)

    if card.Deck in decks:
        decks[card.Deck].append(card)
    else:
        decks[card.Deck] = [card]    

generate_back()

for name, cards in decks.items():
    generate_deck(name, cards)

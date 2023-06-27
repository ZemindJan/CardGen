from text.split_csv import split_csv_line
from card import Card
from generate_card import generate_card, generate_back
from deck import generate_deck
from settings import Settings

with open('data.csv') as f:
    data = f.read()

lines = data.split('\\r\\n')

arg_line = split_csv_line(lines[0])
cards: list[Card] = []

for line in lines[1:]:
    args = split_csv_line(line)

    while len(args) < len(arg_line):
        args.append('')

    if args[0] == '':  # skip empty lines
        continue

    if Settings.use_speed_value:
        cards.append(Card(
            name=args[0],
            god=args[1],
            suite=args[2],
            effect=args[3],
            speed=int(args[4]),
            deck=args[5],
        ))
    else:
        cards.append(Card(
            name=args[0],
            god=args[1],
            suite=args[2],
            effect=args[3],
            speed=None,
            deck=args[4],
        ))

decks = {}

for card in cards:
    generate_card(card)

    if card.deck in decks:
        decks[card.deck].append(card)
    else:
        decks[card.deck] = [card]

generate_back()

for name, cards in decks.items():
    generate_deck(name, cards)

from card import Card
from generate_card import generate_card
from constants import *

for suite in (ROCK, PAPER, SCISSORS):
    generate_card(Card(
        name=f'Heavy {suite}',
        god='Artemis',
        suite=suite,
        effect='5 #dmg and such. 3 #rage. this is some text',
        speed=99,
        deck=None,
    ))

from card import Card
from generate_card import generate_card
from constants import *

for suite in (ROCK, PAPER, SCISSORS):
    generate_card(Card(
        Name=f'Heavy  {suite}',
        God='Artemis',
        Suite=suite,
        Effect='5 #dmg',
        Speed=99,
        Deck=None,
    ))

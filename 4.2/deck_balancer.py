# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('4.2')

from cardsmith import *
from data.source import OnlineSource, ManualSource
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from elements.ellipse import EllipseElement
from elements.text import TextElement
from elements.image import ImageElement
from settings import Settings
from elements.shape import Outline
from elements.mirror import MirrorElement
from keywords import preprocess_fields
from elements.group import GroupElement
from dataclasses import dataclass

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfcuVJtXMn4PGIY7id1qMlOi4IbkVqFpqSArPBe-YZlKZ2crQuPx_IzHGe5O8z86uPB93QAykHNT4T/pub?gid=559014483&single=true&output=csv'

src = OnlineSource(url)
deck_property = 'deck'
suit_property = 'suit'
count_property = 'copies'
acost_property = 'acost'
dcost_property = 'dcost'

@dataclass
class Deck:
    name : str
    high_cards : int
    mid_cards : int
    low_cards : int
    skill_cards : int
    total : int

    def could_be_heavyweight(self):
        return self.high_cards >= 4 and \
            self.mid_cards >= 6 and \
            self.low_cards >= 6 and \
            self.skill_cards >= 6 and \
            self.total == 30
    
    def could_be_middleweight(self):
        return self.high_cards >= 4 and \
            self.mid_cards >= 6 and \
            self.low_cards >= 4 and \
            self.skill_cards >= 8 and \
            self.total == 30
    
    def could_be_lightweight(self):
        return self.high_cards >= 6 and \
            self.mid_cards >= 6 and \
            self.low_cards >= 4 and \
            self.skill_cards >= 6 and \
            self.total == 30

decks : dict[str, Deck] = {}

for entry in src.get_data():
    if deck_property not in entry:
        continue

    deck_name = entry[deck_property]

    if deck_name not in decks:
        decks[deck_name] = Deck(deck_name, 0, 0, 0, 0, 0)

    deck = decks[deck_name]
    suit = entry[suit_property]
    count = int(entry[count_property])
    
    if suit == 'High'   or (suit == 'Multi' and entry['high'] == 'X'):
        deck.high_cards += count
    if suit == 'Middle' or (suit == 'Multi' and entry['mid'] == 'X'):
        deck.mid_cards += count
    if suit == 'Low'    or (suit == 'Multi' and entry['low'] == 'X'):
        deck.low_cards += count
    if suit == 'Skill':
        deck.skill_cards += count

    deck.total += count

for deck in decks.values():
    print(f'-----')
    print(f'{deck.name.upper()}')
    print(f'High Cards:   {deck.high_cards}'.ljust(18) + f'Attack Costs'.ljust(12) + f'Defense Costs')
    print(f'Mid Cards:    {deck.mid_cards}'.ljust(18) + f'0 Cost: '.ljust(12) + f'0 Cost: ')
    print(f'Low Cards:    {deck.low_cards}'.ljust(18) + f'1 Cost: '.ljust(12) + f'1 Cost: ')
    print(f'Skill Cards:  {deck.skill_cards}'.ljust(18) + f'2 Cost: ')
    print(f'Total Cards:  {deck.total}'.ljust(18) + f'3+ Cost: ')
    
    print(f'HeavyWeight:  {"✅" if deck.could_be_heavyweight() else "❌"}')
    print(f'MiddleWeight: {"✅" if deck.could_be_middleweight() else "❌"}')
    print(f'LightWeight:  {"✅" if deck.could_be_lightweight() else "❌"}')
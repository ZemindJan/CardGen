from dataclasses import dataclass

@dataclass
class Card:
    Name : str
    Type : str
    BaseEffect : str
    ExtraWinEffect : str
    Deck : str
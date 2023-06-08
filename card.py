from dataclasses import dataclass


@dataclass
class Card:
    Name: str
    God: str
    Suite: str
    Effect: str
    Speed: int
    Deck: str

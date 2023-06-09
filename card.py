from dataclasses import dataclass


@dataclass
class Card:
    name: str
    god: str
    suite: str
    effect: str
    speed: int
    deck: str

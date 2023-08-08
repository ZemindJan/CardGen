

class Card:
    def __init__(self, path : str, count : int) -> None:
        self.name = path
        self.count = count

class Deck:
    def __init__(self, name : str, cards : list[Card] = None) -> None:
        self.name = name
        self.cards = cards or []
        self.size = sum((card.count for card in self.cards))

    def add_card(self, card : Card):
        self.cards.append(card)
        self.size += card.count

    def get_flat_card_list(self) -> list[Card]:
        cards : list[Card] = []

        for card in self.cards:
            for _ in range(card.count):
                cards.append(card)
        
        return cards
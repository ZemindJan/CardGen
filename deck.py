from generate_card import *

def generate_deck(name: str, cards: list[Card]):
    files = [f'{CARDS_DIR}/{card.Name}.png' for card in cards]

    Y_GRID_SIZE = 2
    X_GRID_SIZE = (len(cards) + 1) // 2

    new_image = Image.new('RGBA', size=(
        size.x * X_GRID_SIZE, size.y * Y_GRID_SIZE))

    for i, file in enumerate(files):
        x_coord = i // 2
        y_coord = i % 2

        image = Image.open(file)
        new_image.paste(image, (size.x * x_coord, size.y * y_coord,
                        size.x * (x_coord + 1), size.y * (y_coord + 1)))
        # Because minimum exports are 2 high, we double the height

    new_image.save(f'{DECKS_DIR}/{name}.png')

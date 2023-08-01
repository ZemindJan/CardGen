from core.geometry import Point, Rect
from core.text.string_parser import replace_references
from core.color import Color, White, verify_color
from PIL import Image, ImageDraw
from core.create_directories import verify_directories
from settings import Settings
from data.source import Source

DEFAULT_DIMENSIONS = Point(2.5 * 96 * 2, 3.5 * 96 * 2)

class Schema:
    def __init__(
            self, 
            naming : str, # this defines how output cards are named. 
            elements : list,
            back_elements : list = None, 
            dimensions : Point = None, 
            background : Color = None, 
            deck_name : str = None, 
            group_by : str = None, 
            deck_grid_size : Point = None,
            required_entry_fields : list[str] = None,
            text_replacements : dict[str, str] = None,
        ) -> None:
        self.naming = naming
        self.dimensions = dimensions or DEFAULT_DIMENSIONS
        self.elements   = elements   or []
        self.back_elements = back_elements or []
        self.background = verify_color(background or White)
        self.deck_name = deck_name
        self.group_by = group_by
        self.deck_grid_size = deck_grid_size or Point(10, 7)
        self.required_entry_fields = required_entry_fields or []
        self.replacements = text_replacements or dict()

    def draw_card(self, entry : dict[str, str], index = 0) -> str:
        image = Image.new(
            mode='RGBA', 
            size=self.dimensions.int_tuple(), 
            color=self.background.tuple()
        )

        for element in self.elements:
            element.draw(image, entry, self, Point.zero().to(self.dimensions))

        name = replace_references(self.naming, entry, index)
        path = f'{Settings.CardsDirectory}/{name}.png'
        verify_directories(path)
        image.save(path)

        return name
    
    def draw_back(self) -> str:
        image = Image.new(
            mode='RGBA', 
            size=self.dimensions.int_tuple(), 
            color=self.background.tuple()
        )

        for element in self.back_elements:
            element.draw(image, {}, self, Point.zero().to(self.dimensions))
        
        path = f'{Settings.CardsDirectory}/back.png'
        verify_directories(path)
        image.save(path)

    def is_viable_entry(self, entry : dict[str, str]) -> bool:
        for field in self.required_entry_fields:
            if field not in entry:
                return False
        
        return True
    
    def replace_text(self, my_string : str) -> str:
        for key, val in self.replacements.items():
            my_string = my_string.replace(key, val)

        return my_string    
    
    def process_entry(self, entry : dict[str, str]) -> dict[str, str]:
        return {key : self.replace_text(val) for (key, val) in entry.items()}

    def process(self, source : Source):
        decks : dict[str, list[str]] = {}
        entries = [self.process_entry(entry) for entry in source.get_data() if self.is_viable_entry(entry)]
        default_deckname = self.deck_name or Settings.GlobalDeckName

        if len(entries) == 0:
            raise Exception('No viable entries!')

        for index, entry in enumerate(entries):
            name = self.draw_card(entry, index)

            if self.group_by:
                group = replace_references(self.group_by, entry, index)
            
                if group not in decks:
                    decks[group] = []

                decks[group].append(name)
            else:
                if default_deckname not in decks:
                    decks[default_deckname] = []

                decks[default_deckname].append(name)

        self.draw_back()
            
        
        self.build_decks(decks)

    def build_decks(self, decks : dict[str, list[str]]):
        for deck, cards in decks.items():
            self.build_deck(deck, cards)

    def build_deck(self, name : str, cards : list[str]):
        cards_per_sheet = self.deck_grid_size.x * self.deck_grid_size.y - 1

        if len(cards) <= cards_per_sheet:
            self.build_cardsheet(name, cards, self.deck_grid_size)
        else:
            sheet_num = (len(cards) + cards_per_sheet - 1) // cards_per_sheet
            for i in range(sheet_num):
                self.build_cardsheet(f'{name}{i+1}', cards[cards_per_sheet * i : cards_per_sheet * (i + 1)], self.deck_grid_size)

    def build_cardsheet(self, name : str, cards : list[str], grid_size : Point):
        sheet = Image.new('RGBA', size=(
            int(self.dimensions.x * grid_size.x), int(self.dimensions.y * grid_size.y)
        ))

        for i, card in enumerate(cards):
            x_coord = i % grid_size.x
            y_coord = i // grid_size.x
            file = f'{Settings.CardsDirectory}/{card}.png'

            image = Image.open(file)
            sheet.paste(image, (int(self.dimensions.x * x_coord), int(self.dimensions.y * y_coord),
                            int(self.dimensions.x * (x_coord + 1)), int(self.dimensions.y * (y_coord + 1))))
            
        # Paste back
        i += 1
        x_coord = i % grid_size.x
        y_coord = i // grid_size.x
        file = f'{Settings.CardsDirectory}/back.png'

        image = Image.open(file)
        sheet.paste(image, (int(self.dimensions.x * x_coord), int(self.dimensions.y * y_coord),
                        int(self.dimensions.x * (x_coord + 1)), int(self.dimensions.y * (y_coord + 1))))
        
        path = f'{Settings.DecksDirectory}/{name}.png'
        verify_directories(path)
        sheet.save(path)
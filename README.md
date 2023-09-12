This is Cardsmith, a tool created to generate cards from .csv files. It was created as a way of speeding up iteration for playtesting, in particular for Tabletop Simulator.

Cards are outputed as individual png files in the cards directory and are combined into sheets of cards in the decks directory.

# How To Use Cardsmith
Cardsmith allows you to define a `Schema`, which tells the generator how a card should be drawn, and allows it to create cards using that schema and rows in a csv file as input. If you want to figure things out I recommend taking a look at `tests/test_text.py` which uses almost every feature in the generator. Also, look at the code! It's simpler than you may think, and should tell you about what's going on. Really this is just wrapping around the Pillow library for image manipulation.

## Setup
This project uses `pipenv` as its dependency manager. You can find many resources online on how that works (e.g. https://realpython.com/pipenv-guide/). 

Currently you just need Pillow but that may change at some point. But for now, `pip install pillow` should do the trick.

## Settings
Various settings and output directories can be changed by modifying the `Settings` object from `core.settings`. I recommend importing this object and changing its values in the same file before you define your schema.

## Sources
First, there are three ways you can fetch your data. They are defined in `data/source.py`. 
* `OnlineSource` allows you to fetch your csv via an online link. This is super useful when paired with Google Sheets, which allows you to publish your data to web as a csv. That way you can edit your Google Sheet, and once it syncs up (it may take a minute or two), the generator will use your new data to create cards.
* `LocalSource` allows the generator to open a csv file you have locally on your machine.
* `ManualSource` allows you to enter the data manually in python. It is primarily meant for debugging, but if you want to use python dicts rather than a csv file, be my guest.

## Schema
This is the core of your card generator. It is constructed with the following fields: 
* `naming` defines how your output cards will be named. If you want it to reflect an entry field like a name, look at the Entry Fields section below.
* `elements` is a list of visual elements to build the card
* `back_elements` is a list of visual elements to build the back of a card. In this version it cannot get any entry data, and is the same for every card. 
* `dimensions` is the size of a card. 
* `background` is the background color. You can use strings for hex codes or to reference the color atlas.
* `deck_name` is the name of the deck file produced if the cards aren't being grouped 
* `group_by` is used to separate cards into different decks- by default it is None, meaning all cards are put into the same deck. Usually you'll want to do this by accessing an entry field, like `$deck$`
* `deck_size_grid` defines the size of the card sheets when decks are produced. By default, it is tabletop sim's largest allowed size, 10x7. Don't worry if you have more cards though- the generator will create multiple decksheets labeled `1` to `n` if needed. 
* `required_entry_fields` is a list of field names you require for an entry to be valid. This is mainly used to filter malformed entries in case you formatted your google sheets in special ways. For example `["name"]` would require all your entries to have data in a field `"name"`, which allows you to access it using `$name$`.  

## Elements
There are various elements in the `elements` folder for you to add to your cards.
* The two shapes currently are `RectElement` and `EllipseElement`, both of which allow for color fill and outlines. They also allow for child elements, so the `RectElement` is particularly useful to subdivide the card. You can also use `make_invisible` to make the element itself not visible, but still show the children. 
* The `TextElement` is the bread and butter of the generator, used for generating text. If the text doesn't fit, it tries to break it into lines, and if the lines won't fit, it'll start making the text smaller until it finds a solution or gives up at 10p. Note that if you want your text to fit into a defined area, sort of like a text box, I recommend making it the child of a `RectElement` whose size your define.
* The `ConditionalElement` is very powerful if you want to do conditional formatting. It will use certain elements if a condition holds or others if it does not. For example, if you want only `heart` cards to have a heart image, you could have `condition='$suite$=heart'` and put the image element for the heart in the `on_true` elements. Right now I only support checking for equality, but I'll add more conditional stuff as I work on this project.
* The `ImageElement` pastes images from the image directory. Note that it has to fit in the images area, though I may change that at some point.

### Scaling Elements
When defining the scaling for elements, you can use PARENT (as defined in `core/scaling.py`) in an equation to scale an element relative to its parents. For example, `PARENT * 0.5` defines an element scaled to half of its parents size in that dimension.

## The Text Processor

### Entry Fields
Entries are processed to have fields, which are defined at the top row of the csv files as the column names. Often you might have columns named *Name* or *Cost*, etc.

One of the primary uses of the generator is to get custom data from entries. To display entry data in text, use `$<name>$` to fetch the entry's data under the field `<name>`. 

To get the card's index in the list of entries, use `$index$`. Entries are processed top-down. Note that this doesn't necessarily correspond to line number if some entries are filtered out for being incomplete.

### Icons
To display images in line with text, you can define icons. They are placed using `#iconname` where the `iconname` must be defined to map to an image in the **Icon Atlas**.

### Tags
There are a few tags you can use in text. Note that- with the exception of `<br>`- all tags that are opened can be closed with `</tagname>`
* `<br>` defines a line break
* `<size=X>` sets the font size
* `<font=X>` sets the font name
* `<color=X>` or `<fill=X>` sets the color of the text. The color can be a hex code or defined in the **Color Atlas**.
* Any other tag is considered to be a font mapping, which changes your text from one font to another. The two most common of these would be `<bold>` and `<italic>`, which will map a font to its bold or italic equivalent, as defined in the **Font Atlas.**

In the future, I will likely add support for tags that set multiple parameters at once.

## The Atlases
An important detail for the generator is the Atlases, which tell it where to find important data. These are the **Font Atlas**, the **Icon Atlas**, and the **Color Atlas**. The font atlas defines names for fonts as well as mappings for tags, such as `<bold>` or `<italic>`. The icon atlas tells the generator what icon corresponds to what image. Finally, the color atlas defines colors by name- they may be RGB or RGBA hex codes, tuples in RGB or RGBA format, or `Color` objects.

Currently compositing non-opaque layers does not work properly. I may look into this in the future.

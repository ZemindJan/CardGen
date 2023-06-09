# How to get the cards
Run fetch_sheet.py to download latest data. It is stored in the data.csv file.
Run process_data.py to process downloaded data into cards, take from the data file.
The cards will be in the out directory, separate as individual cards and decks.

# Icons
Icons are stored in assets/icons and their filepaths are stored in a dictionary in text/icons.py
They are referenced with a # in front of their name. #dmg loads assets/icons/dmg.png for example.

# Publishing to web 
The way that we pull the csv content from google drive is via a link in fetch_sheet.
This link can be changed, so long it pulls a csv file.
To publish any sheet, go to the file menu in google sheets:
File > Share > Publish to Web
Select the section and csv instead of Web Page
Copy that link into fetch_sheet
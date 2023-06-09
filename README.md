# How to get the cards
Run fetch_sheet.py to download latest data
Run process_data.py to process downloaded data into cards
The cards will be in the out directory

# Publishing to web 
The way that we pull the csv content from google drive is via a link in fetch_sheet.
This link can be changed, so long it pulls a csv file.
To publish any sheet, go to the file menu in google sheets:
File > Share > Publish to Web
Select the section and csv instead of Web Page
Copy that link into fetch_sheet
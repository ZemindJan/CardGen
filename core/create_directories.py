import os
from settings import Settings

def verify_directories(filepath : str):
    index = filepath.rfind('/')

    if index != -1:
        my_path = filepath[:index]
        if my_path != '':
            if not os.path.exists(my_path):
                os.makedirs(my_path)

    for other_path in (Settings.CardsDirectory, Settings.DecksDirectory):
        if not os.path.exists(other_path):
            os.makedirs(other_path)
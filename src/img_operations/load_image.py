import numpy as np
import cv2 as cv
import requests
from dataclasses import dataclass


def open_file(self) -> str:
    '''
    Open a file dialog to select an image.
    :return: the path of the selected image
    '''
    from PyQt6.QtWidgets import QFileDialog
    name = QFileDialog.getOpenFileName(self, 'Open File', '.\\resources\\img','Image Files ( *.bmp  *.gif *.jpg *.jpeg *.png *.pbm *.pgm *.ppm *.xbm *.xpm)')[0]
    print(f"\nImage selected: \033[32m{name.split('/')[-1]}\x1B[37m \
            \n   Width: {cv.imread(name).shape[1]:-4} px\
            \n  Height: {cv.imread(name).shape[0]:-4} px\
            \nChannels: {cv.imread(name).shape[2]:-4}\n")
    return name


def load_image(path: str) -> np.ndarray:
    '''
    Load an image from a path.
    '''
    return cv.imread(path)


# ? url
url = 'https://cataas.com/cat'
filename = 'resources\\img\\cat.jpg'

def load_cat() -> str:
    '''
    Load a cat image from the internet and store it to the resources folder.
    :return: the filename of the cat image
    '''
    request = requests.get(url, stream=True)
    with open (filename, 'wb') as file:
        file.write(request.content)
        img = cv.imread(filename)
        # print('new cat image loaded successfully!')
        # cv.imshow('cat', img)
        # cv.waitKey(200)
        return filename




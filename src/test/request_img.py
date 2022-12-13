import requests
import cv2 as cv


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


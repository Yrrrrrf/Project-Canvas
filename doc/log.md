# Notes Log

### September 2th, 2022
First log
Config environment, install dependencies, create project
Create a README.md

### September 4th, 2022
I've decice to change do not use raylib as GUI library because it's not a good idea to use a library that is not in the standard library of the language, (and there's not many code examples in the internet) so I'm going to use the standard library of python, tkinter, to create the GUI.

### September 9th, 2022
Implement whiteboard & mouse position detection.
Still need to implement the file & image reader. I'm going to use the Pillow library to read the image and convert it to a numpy array to manipulate the image.

### September 10th, 2022
Looking for a way to convert the image to a np.array.
I found that the Pillow library has a method called `load()` that returns a `Image` object, and this object has a method called `getdata()` that returns a `ImageData` object, and this object has a method called `getdata()` that returns a `tuple` with the RGB values of the image, so I'm going to use this method to convert the image to a numpy array.

### September 11th, 2022
Implemented image reader and current pixel detection(with mouse).
Still need to implement the pixel's value detection to get the color of the pixel.
Now I need to implement the image to numpy array converter and the neiborhood value detection. 


### November 29th, 2022
Design UML class 

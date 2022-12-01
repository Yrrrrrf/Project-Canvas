# import os, sys  # For the path
import math
from PIL import Image 

# Open the image
img = Image.open('project/resources/img/guardians450.jpg')  # Not a numpy array
# img.show()  # show Images on external default viewer
print(type(img))  # <class 'PIL.JpegImagePlugin.JpegImageFile'>
print(img. size)  #image size (width, height)
print(img.format)  # image format (.jpg, .png, .gif, etc.)
print(img.mode)  # image mode (P=Pallettised (3*8bits RGB), L=Luminositi (8bit grayscale))

# img.show()


# Logarithmic transformation
new_img = img.point(lambda x: (64 * math.log(1+x)))
new_img.show()


# Power Transformation
new_img = img.point(lambda x: (64 * math.pow(x, 2)))
new_img.show()

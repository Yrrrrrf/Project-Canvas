# import os, sys  # For the path
from PIL import Image 

# sys.path.append(os.path.abspath(os.path.join('..', 'config')))
img_path = "project/resources/img/"
save_path = "project/resources/img/archive/"

# Open the image
img = Image.open(img_path+"lena.jpg")  # Not a numpy array
# img.show()  # show Images on external default viewer
print(type(img))  # <class 'PIL.JpegImagePlugin.JpegImageFile'>
print(img. size)  #image size (width, height)
print(img.format)  # image format (.jpg, .png, .gif, etc.)
print(img.mode)  # image mode (P=Pallettised (3*8bits RGB), L=Luminositi (8bit grayscale))

# img.show()
# Increse the contrast
new_img = img.point(lambda x: x*0.5 + 20)
new_img.show()

# Increses the brightness
new_img = img.point(lambda x: x+155)
new_img.show()




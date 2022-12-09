import cv2


# img = cv2.imread('resources\\img\\lena.jpg')
img = cv2.imread('resources\\static\\brush_256.png')

# img.resize(300, 300)
cv2.imshow('image', img)
print(img.shape)



cv2.waitKey(0)
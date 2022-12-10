import cv2


# img = cv2.imread('resources\\img\\lena.jpg')
img = cv2.cvtColor(cv2.imread('resources\\static\\brush_256.png'), cv2.COLOR_BGR2RGB)  # convert to rgb

# img.resize(300, 300)
r, g, b = cv2.split(img)
cv2.imshow('r', r)
cv2.imshow('g', g)
cv2.imshow('b', b)

cv2.imshow('image', img)
print(img.shape)



cv2.waitKey(0)
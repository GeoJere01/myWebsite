import cv2 as cv

img = cv.imread('pictures/cat.jpg')
cv.imshow('Cat', img)

# converting BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur, 100, 170)
cv.imshow('Canny edges', canny)

# dilating an image

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# Resize

resized = cv.resize(img, (580, 580), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

cv.waitKey(0)
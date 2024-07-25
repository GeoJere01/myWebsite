import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# paint image a certain color
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# img = cv.imread('pictures/cat.jpg')
# cv.imshow('Cat', img)

# draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), cv.FILLED)
# cv.imshow('Rectangle', blank)

# # draw a circle
# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,255,0), 3)
# cv.imshow('Circle', blank)

# write text on an image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 3)
cv.imshow('Text', blank)

cv.waitKey(0)



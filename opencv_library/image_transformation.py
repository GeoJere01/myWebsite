import cv2 as cv
import numpy as np

img = cv.imread('pictures/cat.jpg')
cv.imshow('Cat', img)

# translation means shifting along x or y

def translate(img, x, y):
    # translation matrix
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

# translated = translate(img, -100, 100)
# cv.imshow('Translated', translated)

# rotate
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated_image = rotate(img, 45)
cv.imshow('Rotated image', rotated_image)

cv.waitKey(0)
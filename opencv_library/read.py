import cv2 as cv

# reading images
# img = cv.imread('pictures/cat.jpg')
# cv.imshow('Cat', img)

# cv.waitKey(0)

# # reading videos
# capture = cv.VideoCapture('videos/dog.mp4')

# # reading frame by frame of the video
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break

# capture.release()
# cv.destroyAllWindows()  

# resizing an image
# def changeRes(width, height):
#     # only works for live video not standlone videos(videos that already exist)
#     capture.set(3, width)
#     capture.set(4, height)


# def rescaleFrame(frame, scale=0.75):
#     # this method works for images, videos and live videos
#     height = int(frame.shape[0] * scale)
#     width = int(frame.shape[1] * scale)
#     dimensions = (width, height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# # reading videos
# capture = cv.VideoCapture('videos/dog.mp4')

# # reading frame by frame of the video
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame, scale=0.30)
#     cv.imshow('Video_before_resized', frame)
#     cv.imshow('Video_resized', frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break

# capture.release()
# cv.destroyAllWindows()

## DRAWING SHAPES & PUTTING TEXT


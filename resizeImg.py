# Was getting tired of having to manually resize visual examples when doing this so decided to just make a separate file
# that holds a single function for that exact purpose. Should've done this far soon but it is what it is.

import cv2
import imutils
from screeninfo import get_monitors
from multiprocessing.sharedctypes import Value


# Function to reduce an image to half it's size while still maintaining it's aspect ratio
def imgResizeHalf(img_path, title):
    img = cv2.imread(img_path)
    img_w = img.shape[1]
    img_h = img.shape[0]
    monitor = get_monitor_info()


    # Check to see if the image width and height is larger than the monitor's dimensions, if so resize it before continuing
    if img_w > monitor[0] and img_h > monitor[1]:
        # Set the height and width to be the exact heigh of the monitor's width by subtracting the difference of the two from it
        img_w -= monitor[0]
        img_h -= monitor[1]
        # To make sure the forefront of the desktop doesn't cover the image, an extra 100 pixels is subtracted before resizing
        img = imutils.resize(img, width=int(img_w - 300))
        img = imutils.resize(img, height=int(img_h - 300))
    else:
        img_w = img_w/2
        img_h = img_h/2
        img = imutils.resize(img, width=int(img_w), height=int(img_h))

    cv2.imshow(title, img)
    cv2.waitKey(0)



# Gets the dimensions of the main monitor to know whether file needs to be re
def get_monitor_info():
    # Returns the primary monitor's width and height
    return (get_monitors()[0].width, get_monitors()[0].height)
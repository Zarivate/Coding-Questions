# Was getting tired of having to manually resize visual examples when doing this so decided to just make a separate file
# that holds a single function for that exact purpose. Should've done this far soon but it is what it is.

import cv2
import imutils
from screeninfo import get_monitors
from multiprocessing.sharedctypes import Value

def imgResizeHalf(img):
    img_w = img.shape[1]
    img_h = img.shape[0]
    monitor = get_monitor_info()


# Gets the dimensions of the main monitor to know whether file needs to be re
def get_monitor_info():
    # Returns the primary monitor's width and height
    return (get_monitors()[0].width, get_monitors()[0].height)
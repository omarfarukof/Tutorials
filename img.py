import cv2
import numpy as np

# import os
# os.environ['QT_QPA_PLATFORM'] = 'xcb'

img = cv2.imread("assets/image.jpg" )
## Show the image   
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# import os
# os.environ['QT_QPA_PLATFORM'] = 'xcb'

# img = cv2.imread("assets/image.jpg" )
# ## Show the image   
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from OpenCV_Simple.OpenCV_Simple import *

img = read_cv("assets/image.jpg" , 1)
# img = rotate_cv(img , 90)
# img = cv2.rotate(img)
img = rotate_cv(img , -1)
# print_cv( resize_cv(img , 500 , 700) )
# print_cv(img)
x , y , z = img.shape
print(x, y , z)
show_cv( resize_cv(img , round(x) , round(y) ) )
show_cv( resize_cv(img , round(x*0.25) , round(y*0.25) ) )
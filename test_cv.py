from OpenCV_Simple.OpenCV_Simple import *

# Solve Linux QT Error
qt_error()

# Main Test

# video_cv(0)
def video(source):
    return cv2.VideoCapture(source)

# cap = video(0)

# def show_video(cap , title = 'Frame' , wait = 0):

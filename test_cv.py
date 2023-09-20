from OpenCV_Simple.OpenCV_Simple import *

# Solve Linux QT Error
qt_error()

# Main Test

# video_cv(0)
def video(source):
    return cv2.VideoCapture(source)

def video_break(wait = 1 , exit_key = 'q'):
    return cv2.waitKey(wait) == ord(exit_key)


def show_video(cap , title = 'Frame' , wait = 1 , exit_key = 'q'):
    while True:
        ret, frame = cap.read()
        
        cv2.imshow("Video", frame)
        # show_cv(cap , title="Video Capture" , raw = True)
        if video_break():
            break

def fill_cv(shape , value):
    # return np.zeros(shape , np.uint8)
    return np.ones(shape , np.uint8)*value

cap = video(0)

# show_video(cap)

while True:
    ret, face = cap.read()

    frame = fill_cv(face.shape , 0)
    face = resize_cv( face , scale=0.5 )

    frame[0:face.shape[0] , 0:face.shape[1]] = face
    frame[face.shape[0]: , face.shape[1]:] = rotate_cv(face , -2)
    frame[face.shape[0]: , 0:face.shape[1]] = resize_cv( rotate_cv(face , -1) , face.shape[0] , face.shape[1] )
    
    cv2.imshow("Video" , frame)

    if video_break():
        break


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

    height = int( cap.get(4) )
    width = int( cap.get(3) )

    # frame = fill_cv(face.shape , 0)
    frame = face

    # face = resize_cv( face , scale=0.5 )
    # frame[0:face.shape[0] , 0:face.shape[1]] = face
    # frame[face.shape[0]: , face.shape[1]:] = rotate_cv(face , -2)
    # frame[face.shape[0]: , 0:face.shape[1]] = resize_cv( rotate_cv(face , -1) , face.shape[0] , face.shape[1] )


    img = cv2.line(frame , (0,0) , (width , height) , (255,0,0) , 10 )
    img = cv2.line(img , (width,0) , (0 , height) , (55,0,100) , 10 )
    # img = cv2.rectangle(img , (width/2,height/2) , (width*2/3,height*2/3) , (100,100,100) , 5 )
    
    img = cv2.rectangle(img , (width//3,height//3) , (width*2//3,height*2//3) , (100,100,100) , 5 )
    img = cv2.circle( img , (width//2 , height//2 - 100) , 50 , (0,0,100) , -1 )

    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText( img , "Hello, Omar ?" , (width-600,height-100) , font , 2 , (10,10,10) , 5 , cv2.LINE_AA )

    cv2.imshow("Video" , img)

    if video_break():
        break


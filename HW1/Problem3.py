import torch
import time
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def gstreamer_pipeline(
    capture_width=1920,                                     # Set to your camera's highest resolution
    capture_height=1080,
    display_width=224,
    display_height=224,
    framerate=30,                                          # Set the value according to your camera
    flip_method=0,
):
    return (
        'nvarguscamerasrc sensor_mode=0 ! '
        'video/x-raw(memory:NVMM), '
        'width=(int)%d, height=(int)%d, '
        'format=(string)NV12, framerate=(fraction)%d/1 ! '
        'nvvidconv flip-method=%d ! '
        'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
        'videoconvert ! '
        'video/x-raw, format=(string)BGR ! appsink'
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def camDet(cap):

    frame_rate_calc = 1
    freq = cv2.getTickFrequency()

    while(True): 
        
        t1 = cv2.getTickCount()

        # Capture frame-by-frame
        ret, frame = cap.read()

        #result = model(frame)

        # Display the resulting frame
        cv2.imshow("preview",frame)
        #cv2.imshow("output", result)

        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate_calc= 1/time1

        #Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Open the device
vid = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

#Check whether user selected camera is opened successfully.
if not (vid.isOpened()):
    print("Could not open video device")

if vid.isOpened():
    camDet(vid)

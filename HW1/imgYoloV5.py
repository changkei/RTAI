import torch
import time
import cv2
#print(torch.__version__)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def imageDet(img_dir, batchS):
    timeS = []
    x = 1
    img = ''
    if batchS == 1:
        while x < 16:
            img = img_dir + str(x) + '.jpg'
            start = time.time()
            result = model(img)
            end = time.time()
            duration = end - start
            timeS.append(duration)
            x = x + 1
    elif batchS == 8:
        while x < 3:
            if x == 1:
                img = [img_dir + f for f in ('1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg')]
            elif x == 2:
                img = [img_dir + f for f in ('9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg')]
            start = time.time()
            result = model(img)
            end = time.time()
            duration = end - start
            timeS.append(duration)
            x = x + 1
    elif batchS == 16:
        img = [img_dir + f for f in ('1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg')]
        start = time.time()
        result = model(img)
        end = time.time()
        duration = end - start
        timeS.append(duration)

    totalTime = 0
    for i in range(0, len(timeS)):
        totalTime = totalTime + timeS[i]
    
    #Print time in seconds
    print(totalTime)

dir = '/home/keith/Pictures/'
batchSizeO = 1
batchSizeE = 8
batchSizeS = 16
imageDet(dir, batchSizeO)
imageDet(dir, batchSizeE)
imageDet(dir, batchSizeS)


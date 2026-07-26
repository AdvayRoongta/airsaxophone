import cv2 as cv
import numpy as np
camera=cv.VideoCapture(0)#webcam
camera.set(cv.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
prev=None
dist= lambda x1,y1,x2,y2: (x1-x2)**2+(y1-y2)**2

while True:
    sucess,frame= camera.read()
    if sucess == False:
        break
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #gray and blur the frame
    blur=cv.GaussianBlur(gray,(9,9),2) #maybe get rid of the blurs for actuall use because blurring the table wont do anything. but it would help in case of the net so we'll see.
    circles= cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1.2,480,param1=100, param2=20, minRadius=5, maxRadius=40) #mess with 1.2(dp), maybe params2 (points on edge to define), radius's
    print(circles)#
    if circles is not None: #if there are cirlces, circles var is a list
        circles=np.uint16(np.around(circles))
        chosen=None
        for i in circles[0,:]:
            x,y,r=i
            mask= np.zeros_like(blur)
            cv.circle(mask, (x, y), r, 255, -1)
            mean = cv.mean(blur, mask=mask)[0]
            if mean>150: 
                chosen=i 
            else: 
                continue 
           # print(circles) 
            if chosen is None: chosen =i 
            if prev is not None: 
                if dist(chosen[0],chosen[1],prev[0],prev[1])<= dist(i[0],i[1], prev[0],prev[1]):
                    
                    pass
            x,y,r=chosen          
            cv.circle(frame,(x,y),r, (255,0,0), 4 )
            prev=chosen
            
    cv.imshow("asdf",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
camera.release()


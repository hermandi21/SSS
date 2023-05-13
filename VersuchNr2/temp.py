import numpy as np
import time
import cv2


cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,150)
cam.set(12,32)




print("frame width: " + str(cam.get(3)))
print("frame height: " + str(cam.get(4)))
print("--------------------------------")
print("brightness: " + str(cam.get(10)))
print("contrast: " + str(cam.get(11)))
print("saturation: " + str(cam.get(12)))
print("--------------------------------")
print("gain: " + str(cam.get(14)))
print("exposure: " + str(cam.get(15)))
print("--------------------------------")
print("white balance: " + str(cam.get(17)))

#Routine zur Aufnahme der Bilder
counter = 0
i = 0
while(True):
    ret, frame = cam.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite('schwarzBild' + str(i) + '.png', gray)
            i = i+1
            time.sleep(1)
        if key == ord('q'):
            break;
      

cam.release()
cv2.destroyAllWindows()


import cv2
import numpy as np
detector= cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
i=0
name=raw_input('enter your id:')
id = raw_input('Enter your name please:')
cam = cv2.VideoCapture(0)
while True:
    ret,im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("dataset/"+str(id)+"."+name +'.'+ str(i) + ".png", gray[y:y+h,x:x+w])
        cv2.imwrite("dataset/"+str(id)+"."+name +'.'+ str(i)+'.'+str(i) + ".png", cv2.equalizeHist(gray[y:y+h,x:x+w]))
        ##cv2.imwrite("dataset/"+str(id)+"."+name +'.'+ str(i)+'.'+str(i) +'.'+str(i) + ".jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        cv2.waitKey(100)
    cv2.imshow(str(id),im)
    cv2.waitKey(1)
    if i>50:
        cam.release()
        cv2.destroyAllWindows()
        break
print "Data Set Created!Thank You"

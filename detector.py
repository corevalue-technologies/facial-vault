import cv2
import os
cam = cv2.VideoCapture(0)
detector= cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainningData.yml")
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX
path = 'dataset'
def getName(i):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        if i==ID:
            name= os.path.split(imagePath)[-1].split('.')[0].split('-')[0]
            break
    return name    
while True:
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        if conf<50:
            name = getName(id)
            cv2.putText(img,name, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
            print id,conf
        else:
            cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
    cv2.imshow('im',img)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

import base64
import os
import time
import sys
import win32api
import cv2

def goto(linenum):
    global line
    line = linenum

def set_Password():    
    obj = open("f:\\project\\face recog\\SecretPasswordFile.txt","w")
    obj.write(base64.b64encode(raw_input("Set Your Password: ")))
    obj.close()   
    drive = str(raw_input("Which drive You want to create Locker Folder: "))
    os.chdir(drive)
    if not os.path.exists("Locker"):
            if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.mkdir("Locker")
                sys.exit()
            else:
                sys.exit()
    else:
        sys.exit()
                
if not os.path.exists("f:\\projects\\face recog\\SecretPasswordFile.txt"):
    set_Password()

passwordFile = open('f:\\projects\\face recog\\SecretPasswordFile.txt','r')
pw = passwordFile.read()
passwordFile.close()

encode = base64.b64decode(pw)
path = 'dataset'
def getName(i):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        if i==ID:
            name= os.path.split(imagePath)[-1].split('.')[0].split('-')[0]
            break
    return name    
def detector():
    cam = cv2.VideoCapture(0)
    detector= cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("recognizer\\trainningData.yml")
    id = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    path = 'dataset'
    flag = 0
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
                win32api.MessageBox(0, 'Your folder unlocked Successfully', 'Success')
                print id,conf
                flag = 1
            else:
                cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
               ##win32api.MessageBox(0, 'unorthrised user', 'failed')
        cv2.imshow('im',img)
        if cv2.waitKey(1)==ord('q') or flag == 1 :
            break
    cam.release()
    cv2.destroyAllWindows()
    return

def reset_password():
    password = str(raw_input("Enter your current password: "))
    if password == encode:
        obj = open("f:\\projects\\face recog\\SecretPasswordFile.txt","w")
        obj.write(base64.b64encode(raw_input("Set Your Password: ")))
        obj.close()
        win32api.MessageBox(0, 'Your password Successfully Reset', 'Password')
        sys.exit()
    else:
        win32api.MessageBox(0, 'Your current password does not match', 'Password')
        os.system('cls')
        reset_password()
        

line = 1
while True:
    pw = str(raw_input("Enter your password for Lock or Unlock your folder: "))
    if pw == "12345":
            reset_password()
    

    if pw == encode:
    # Change Dir Path where you have Locker Folder
        drive = str(raw_input("Which drive You want to access Locker Folder: "))
        os.chdir(drive)
        detector()
    # If Locker folder or Recycle bin does not exist then we will be create Locker Folder
        if not os.path.exists("Locker"):
            if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.mkdir("Locker")
                sys.exit()
            else:
                os.popen('attrib -h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}","Locker")
                sys.exit()
        else:
            os.rename("Locker","Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen('attrib +h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
            sys.exit()
        
    else:
        win32api.MessageBox(0, 'Wrong password!, Please Enter right password', 'Password')
        os.system('cls')
        goto(1)

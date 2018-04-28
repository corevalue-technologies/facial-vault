import cv2

face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
flag = 0
while(True):
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
                roi_gray = gray[y:y+h,x:x+w]
                roi_color = frame[y:y+h,x:x+w]
        cv2.imshow("captured Image",frame)
        k = cv2.waitKey(1)
        if k == 27:
                cap.release()
                cv2.destroyAllWindows()
                break;
        elif k == ord('s'):
                cv2.destroyAllWindows()
                flag = 1;
                cap.release()
                break;
if flag == 1:
        i = raw_input('whose face is this ?')
        print i
        cv2.imwrite('dataset/User.'+str(i)+'.jpg',gray[y:y+h,x:x+w])

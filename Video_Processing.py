#12. LIVE VIDEO FROM WEBCAM
import cv2
cap = cv2.VideoCapture(0) #0 takes default camera of laptop
#for external webcam use 1
while(True):
    ret,frame = cap.read()#reading the data from webcam
    #ret & frame are 2 variables to be taken,but only frame will be used
    #ret is dummy
    cv2.imshow('My Live Sketch',frame)
    if (cv2.waitKey(1) == 13) :
        break #13 is ASCII value of ENTER key
#as soon as you press ENTER key your output will be gone
cap.release() #release the port which was reserved
#if release is not done properly, it might corrupt the webcam drivers
cv2.destroyAllWindows()

#13. LIVE CANNY SKETCH/VIDEO - EDGE DETECTION
import cv2
cap = cv2.VideoCapture(0)
while (True) :
    ret, frame = cap.read()
    canny = cv2.Canny(frame,100,150)#100 is threshold1, 150 is threshold2 for best edge detection
    cv2.imshow("MY CANNY SKETCH",canny)
    if( cv2.waitKey(1) == 13):
        break
#threshold values can be any (0 to 255)
cap.release()
cv2.destroyAllWindows()

#14. FACE RECOGNITION
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #file name exported from open_cv file
img = cv2.imread('abc.jpg') #image of Open_CV folder
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converts into grayscale
faces = face_cascade.detectMultiScale(gray,1.1,9)
#1.1 is scale factor, minNeighbors = 9 <= best possible values found by hit & trial
#minNeighbors - parameter, which specifies how many neighbors each rectangle should retain
#scaleFactor - parameter, which specifies how much image size is reduced
#the lesser the minneighbors & scaleFactor, the more accurate the model is
for x,y,w,h in faces :
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    #x,y - starting point,(x+w,y+h) end point,(0,255,0), 5 - thickness
cv2.imshow("FACE RECOGNITION",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

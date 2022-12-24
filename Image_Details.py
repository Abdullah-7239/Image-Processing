#8. CHECKER BOARD/CHESS BOARD(8X8)
import numpy as np
import cv2
img = np.zeros((200,200,3))
#imf[y=coordinate,x-coordinate]
img[0:100,0:100] = 255,255,255
img[100:200,100:200] = 255,255,255
cv2.imshow('Checker board',img)
cv2.waitKey(0)
cv2.destroyAllwindows()

#9.RGB EXTRACTION from image
import cv2
import numpy as np
img = cv2.imread('abc.jpg')
cv2.imshow("ORGINAL IMAGE",img)
#now we have to create 3 variables
B,G,R = cv2.split(img)
zeros = np.zeros(img.shape[:2],dtype='uint8')#we are only considering the length & width
cv2.imshow('RED',cv2.merge([zeros,zeros,R]))
#it merges red plane with black background
cv2.imshow('GREEN',cv2.merge([zeros,G,zeros]))
#it merges green plane with black background
cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()

#10.EDGE DETECTION - SQBEL, LAPACIAN, CANNY
import cv2
img = cv2.imread('abc.jpg',0)#0 converts to grayscale

laplacian= cv2.Laplacian(img,cv2.CV_8U)
#CV_8U --> unsigned 8 bit per pixel <- mandatory for laplacian
cv2.imshow("Laplacian Image",laplacian)
canny = cv2.Canny(img,90,200)#90 is threshold1 200 is threshold2
cv2.imshow('Canny Image',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

#11. RECTANGLE/SQUARE
import cv2
import numpy as np
img = np.zeros((1000,1000,3)) #black background
#img, start point, end point, color.thickness
cv2.rectangle(img,(200,200),(700,700),(0,0,255),5)
cv2.imshow('Rectangle/Square',img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

 
    

    
    
    



    



    

    
    



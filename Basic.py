#1. READ THE IMAGE
import cv2 #importing opencv library
img = cv2.imread('abc.jpg') #reading the image
cv2.imshow('OUTPUT',img) #it will display the image
#two mandotory lines to always write are given below
cv2.waitKey(3000)#it is for how long will the image stay on screen as output
cv2.destroyAllWindows() #it closes all python output windows if open

#2.CREATE A DUPLICAT IMAGE
import cv2
img = cv2.imread("abc.jpg")#reads the image
cv2.imshow('Original Image',img)#displays the image
cv2.imwrite('duplicate abc.png',img)#duplicates the image into a new image file
cv2.waitKey(0)
cv2.destroyAllWindows()

#3.READ THE INFO AB0UT THE IMAGE
import cv2
img = cv2.imread("abc.jpg")
print(img.shape) #prints image info in format (height, width, depth/channel value(RGB)) in pixels

#4. GRAYSCALE - BLACK & WHITE
import cv2
img = cv2.imread("abc.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #grayscale conversion
cv2.imshow('NORMAL IMAGE',img)
cv2.imshow('GRAYSCALE IMAGE',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#5. BINARY IMAGE CONVERSION (HIGH CONTRAST)
import cv2
img = cv2.imread('abc.jpg',0)#0 converts into grayscale
cv2.imshow("Grayscale Image",img) #before conversion
cv2.waitKey(5000)#after 5 second the above img will be gone and code will continue
cv2.destroyAllWindows()
#cv2.threshold(image source,min value,max value,type  of conversion)
ret,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret is dummy variable which we dont use
cv2.imshow("Binary Image",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

#6.SOLID BACKGROUND
#CREATE WHITE OR BLACK BACKGROUND
import numpy as np
import cv2
img = np.zeros((500,500,3))
#np.ones -> white background color np.zeros -> black background
cv2.imshow("white background",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#7.SOLID COLORS
#REG, GREEN, BLUE
import numpy as np
import cv2
img = np.zeros((500,500,3))#creates a black bckgrnd
img[:] = 0,0,0 #Assigning B.G.R values no need for brackets here
#img[:] selects the whole image
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




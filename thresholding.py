import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while(True):
	_,img= cam.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	x=20
	y=100
	w=300
	h=250

	img2=img[y:y+h,x:x+w]
	
	
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow("original",img)

	#thresholding
	ret, threshold = cv2.threshold(img2,12,255,cv2.THRESH_BINARY)
	grayscaled = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, threshold2 = cv2.threshold(grayscaled, 100,255,cv2.THRESH_BINARY)
	gaus = cv2.adaptiveThreshold(grayscaled, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)

	cv2.imshow("threshold",threshold)
	cv2.imshow("threshold2",threshold2)
	cv2.imshow("adaptive threshold", gaus)


	if(cv2.waitKey(1)==ord('q')):
		break

cam.release()
cv2.destroyAllWindows()
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


	#gradiants
	laplacian = cv2.Laplacian(img2, cv2.CV_64F)
	sobelx = cv2.Sobel(img2 , cv2.CV_64F,1,0, ksize=5)		#vertical
	sobely = cv2.Sobel(img2 , cv2.CV_64F,0,1, ksize=5)		#horizontal

	cv2.imshow("laplacian", laplacian)
	cv2.imshow("sobelx", sobelx)
	cv2.imshow("sobely", sobely)


	if(cv2.waitKey(1)==ord('q')):
		break

cam.release()
cv2.destroyAllWindows()
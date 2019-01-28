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


	#edge detection(canny edge detection)
	edges = cv2.Canny(img2 , 100, 200)

	cv2.imshow("Edges", edges)


	if(cv2.waitKey(1)==ord('q')):
		break

cam.release()
cv2.destroyAllWindows()
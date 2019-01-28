import numpy as np
import cv2



cam = cv2.VideoCapture(0)

while(True):
	ret,img= cam.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	x=20
	y=100
	w=300
	h=250
	
	
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow("face",img)
	if(cv2.waitKey(1)==ord('q')):
		break

cam.release()
cv2.destroyAllWindows()
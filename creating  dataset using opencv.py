import cv2
import numpy as np 

sampleNum = 0

uid = input('enter user id')

cam = cv2.VideoCapture(0)

while(True):
	ret,img = cam.read()	#ret is used to find if the camera is providing the frames or not.....we can ignore this with "_"
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	x=20
	y=100
	w=300
	h=250
	sampleNum+=1
	#creates the gtreen rectangle
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	img2=img[y:y+h,x:x+w]	

	#saving address         
	cv2.imwrite('data set1/'+str(uid)+'_'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])     #create a folder "data set1" in the main directory......saves gray scale images
	cv2.imwrite('data set2/'+str(uid)+'_'+str(sampleNum)+'.jpg',img[y:y+h,x:x+w])       #create a folder "data set2" in the main directory.....saves coloured images



	cv2.waitKey(100)	#there is a gap of 100 miliseconds between every frame caputured

	cv2.imshow('INPUT',img)

	cv2.waitKey(1)
	if(sampleNum>10):
		break
cam.release()
cam.destroyAllWindows()

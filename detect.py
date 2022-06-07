import cv2 
from deepface import DeepFace 

capture = cv2.VideoCapture(0)
while True :
	_, img = capture.read()
	try :
		emotion = DeepFace.analyze(img,actions=['emotions'])
		print(emotion["dominant_emotion"])
	except:
		print("No Face Found")
	cv2.imshow("Emotion Detection",img)
	key = cv2.waitKey(1)
	if key == ord("s"):
		break

capture.release()
cv2.destroyAllWindows()

import numpy
import dlib
import cv2
import face_recognition

load = face_recognition.load_image_file('Lab_Daro.jpg')
load = cv2.cvtColor(load,cv2.COLOR_BGRA2BGR)


faceLoc = face_recognition.face_locations(load)[0]
cv2.rectangle(load,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[1]),(255,0,255),2)
faces_encode = face_recognition.face_encodings(load)[0]
print(faces_encode)

cv2.imshow('Daro',load)
cv2.waitKey(0)
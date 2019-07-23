#http://www.paulvangent.com/2016/06/30/making-an-emotion-aware-music-player/
import cv2
import os
import time
import glob
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
#C:\Users\Riddhim Gupta\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data
face_cascade = cv2.CascadeClassifier("C:\\Users\\Riddhim Gupta\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
facedict = {}
emotions =["anger","disgust","fear","happy","neutral","sad","surprise"]
#To crop face in an image
def crop_face(clahe_image, face):
    for (x, y, w, h) in face:
        faceslice = clahe_image[y:y+h, x:x+w]
        faceslice = cv2.resize(faceslice, (350, 350))
    facedict["face%s" %(len(facedict)+1)] = faceslice
    return faceslice
def build_set(emotions):
    check_folders(emotions)
    for i in range(0, 1):#len(emotions)
        save_face(emotions[i])
    print("Great,You are Done!" )
    cv2.destroyWindow("preview")
    cv2.destroyWindow("webcam")
#To check if folder exists, create if doesnt exists
def check_folders(emotions):
    for x in emotions:
        if os.path.exists("dataset\\%s" %x):
            pass
        else:
            os.makedirs("dataset\\%s" %x)
#To save a face in a particular folder
def save_face(emotion):
    print("\n\nplease look " + emotion)
#To create timer to give time to read what emotion to express
    for i in range(0,5):
        print(5-i)
        time.sleep(1)
    #To grab 50 images for each emotion of each person
    while len(facedict.keys()) < 5:
        open_webcamframe()
    #To save contents of dictionary to files
    for x in facedict.keys():
        cv2.imwrite("dataset\\%s\\%s.jpg" %(emotion,  len(glob.glob("dataset\\%s\\*" %emotion))), facedict[x])
    facedict.clear() #clear dictionary so that the next emotion can be stored

def open_webcamframe():

    while True:
        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False
        cv2.imshow("preview", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"): # exit on ESC
            break
        elif key == ord("c"):
            #To convert image into grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            clahe_image = clahe.apply(gray)
           #To run classifier on frame
            face = face_cascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=15, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
           #To draw rectangle around detected faces
            for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                 #draw it on "frame", (coordinates), (size), (RGB color), thickness 2
#Use simple check if one face is detected, or multiple (measurement error unless multiple persons on image)
                if len(face) == 1:
                    faceslice = crop_face(clahe_image, face)
                    cv2.imshow("webcam", frame)
                    return faceslice#slice face from image
                    cv2.destroyWindow("webcam")
                else:
                    print("no/multiple faces detected, passing over frame")

    cv2.destroyWindow("preview")

build_set(emotions)

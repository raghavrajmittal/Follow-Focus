import cv2
import numpy as np
from goprocam import GoProCamera
from goprocam import constants
import urllib.request
import rotate
import thread

def calculateMiddle(width, boxX, boxWidth):
    return width - (boxX + boxWidth/float(2))

def rotationCoordinates(angle):
    const = 4
    if angle > 0:
        return "L" + str(int(abs(angle/float(const))))
    else:
        return "R" + str(int(abs(angle/float(const))))

width = 863/float(2)

#List of possible classifiers for GoPro recognition 
classfiers = [
   "haarcascade_eye_tree_eyeglasses.xml" , #0
   "haarcascade_eye.xml" , #1
   "haarcascade_frontalcatface_extended.xml" , #2
   "haarcascade_frontalcatface.xml" , #3
   "haarcascade_frontalface_alt_tree.xml" , #4
   "haarcascade_frontalface_alt.xml" , #5
   "haarcascade_frontalface_alt2.xml" , #6
   "haarcascade_frontalface_default.xml" , #7
   "haarcascade_fullbody.xml" , #8
   "haarcascade_lefteye_2splits.xml" , #9
   "haarcascade_licence_plate_rus_16stages.xml" , #10
   "haarcascade_lowerbody.xml" , #11
   "haarcascade_profileface.xml" , #12
   "haarcascade_righteye_2splits.xml" , #13
   "haarcascade_russian_plate_number.xml" , #14
   "haarcascade_smile.xml" , #15
   "haarcascade_upperbody.xml" #16
]
chosenClassifier = classfiers[8]
#Path to classifier
# cascPath varies based on local machine.  /usr/local/share/ is the main difference amongst machines
cascPath="/usr/local/share/opencv/haarcascades/" + chosenClassifier
bodyCascade = cv2.CascadeClassifier(cascPath)


gpCam = GoProCamera.GoPro()
gpCam.gpControlSet(constants.Stream.BIT_RATE, constants.Stream.BitRate.B2_4Mbps)
#gpCam.gpControlSet(constants.Stream.WINDOW_SIZE, constants.Stream.WindowSize.W480)

#Read media buffer from udp port
cap = cv2.VideoCapture("udp://127.0.0.1:10000")

arduino = rotate.connect()


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Classifier attributes
    bodies = bodyCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in bodies:
        diff = calculateMiddle(width, x, w)
        angle = rotationCoordinates(diff)
        rotate.rotate(arduino, angle)
        print(angle)
        break

    # Draw a rectangle around the bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow("GoPro OpenCV", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
rotate.disconnect(arduino)

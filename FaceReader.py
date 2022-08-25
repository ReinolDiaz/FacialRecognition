import cv2
import time
import datetime

#capture of video can be cv2.VideoCapture(X) x being the camera input device can rande from (0-n)
capture = cv2.VideoCapture(0)

#creates cascade to compare video to xml file of machine learning algorithm that has been fed a ton of faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#one for body too
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

image_counter = 0

detection = False
detection_stopper_time = None
timer_started = False
time_to_Record_after_detection = 5

#This while loop opens the window and creates a way to close it by pressing "q"
while True:
    _, frame = capture.read()

    #grayscale is needed for haarcascades
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detectMultiScale uses (grayInput, 1.0-n(the lower the more accurate), (boxes around face to prove that it is valid higer = less faces detected)) 
    faces = face_cascade.detectMultiScale(gray,1.1,7)
    bodies = body_cascade.detectMultiScale(gray,1.1,7)

    #draw a box around faces in image
    for (x,y,width,height) in faces:
        #creates rectangle for the face (location , (top left, bottom right), (color in BGR), Thickness of line)
        cv2.rectangle(frame, (x, y),(x + width, y + height), (255, 0, 0), 3)

    #draw a box around bodies in image
    for (x,y,width,height) in bodies:
        #creates rectangle for the face (location , (top left, bottom right), (color in BGR), Thickness of line)
        cv2.rectangle(frame, (x, y),(x + width, y + height), (0, 0, 255), 3)

    #if face or body detected take a pic
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            #creates image file name
            current_Time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            image_name = "{}.png".format(current_Time)
            #image capture
            cv2.imwrite(image_name, frame)
            print("{} written!".format(image_name))
            image_counter += 1
    elif detection:
        if timer_started:
            if time.time() - detection_stopper_time > time_to_Record_after_detection:
                detection = False
                timer_started = False
                print('Time over')
        else:
            timer_started = True
            detection_stopper_time = time.time()

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()




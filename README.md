FacialRecognition

Simple face recognition feature that snaps a picture if any face has been detected in the frame.

Can be scaled to use multiple cameras and uses CV2 to detect faces.

Has a timer of 5 seconds, if no face has been detected in this time it will snap a new picture once one is detected.

If a face is on the camera and does not go off screen for 5 seconds no more pictures will be taken untill this rule is satisfied.

Pictures are saved in same directory as FaceReader.py(picture directory coming soon).

Can be adapted to record video.

Pictures captures are saved in (day-month-year-hour-minute-second.png) format.

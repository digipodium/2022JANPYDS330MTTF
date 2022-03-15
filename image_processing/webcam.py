import cv2

WEBCAM_IDX = 0

vid = cv2.VideoCapture(WEBCAM_IDX)
while True:
    status, frame = vid.read()
    if status:
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == ord("q"): # check if the user pressed "q" 
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()
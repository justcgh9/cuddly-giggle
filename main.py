import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    frame = cv2.flip(frame, 1)
    
    frame = cv2.resize(frame, (600, 600), interpolation=cv2.INTER_LINEAR)

    frame = cv2.blur(frame, (5, 5))
    
    cv2.imshow('WebCam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()

cv2.destroyAllWindows()

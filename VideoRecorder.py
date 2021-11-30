import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True :
    success, frame = cap.read()

    out.write(frame)

    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xFF == ord('a') :
        break

cap.release()
out.release()
cv2.destroyAllWindows()
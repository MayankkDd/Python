import numpy as np
import cv2

captured_video = cv2.VideoCapture('Compiler design tutorial hindi for gate.mp4')

while(True):

    is_captured, captured_frame =  captured_video.read()
    cv2.imshow('Output Video Player', captured_frame)

    if(cv2.waitKey(1) & 0xFF == 'q'):  # i wonder how this id expression will be evaluated??
        break

captured_video.release()
cv2.destroyAllWindows()
#Obtenido de: https://subscription.packtpub.com/book/application_development/9781785283932/3/ch03lvl1sec28/accessing-the-webcam
import cv2

def tomarFoto():
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")


    while True:

        ret, frame = cap.read()

        cv2.imshow('TC1001S - Evidencia', frame)
        c = cv2.waitKey(1)

        if c == 13:
            break

    # tomar foto
    ret, frame = cap.read()
    while True:

        cv2.imshow('TC1001S - Evidencia', frame)
        c = cv2.waitKey(1)

        if c == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

    return frame

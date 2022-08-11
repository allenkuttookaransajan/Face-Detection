import cv2 as cv

haar_cascade = cv.CascadeClassifier("C:/Users/allen/Desktop/Face recognition/Face Mask/haar_face.xml")

cap = cv.VideoCapture(0)

while True:
    ret ,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for(x,y,w,h) in face:

        color = (0, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)

    cv.imshow('Color', frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
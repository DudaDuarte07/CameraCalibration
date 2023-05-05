import cv2 as cv

cap = cv.VideoCapture(0)

num = 0

while cap.isOpened():

    succes, img = cap.read()

    k = cv.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # s To save de image
        cv.imwrite('images/img' + str(num) + '.png', img)
        print("Image saved!")
        num += 1

    cv.imshow('Img',img)

# Release and destroy all windows before termination
cap.release()

cv.destroyAllWindows()
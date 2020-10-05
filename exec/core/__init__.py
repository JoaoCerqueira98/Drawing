import cv2

def nothing(x):
    print(x)


def foto(cam=0):
    cap = cv2.VideoCapture(cam)
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite('foto.jpg', frame)
            break
    cap.release()
    cv2.destroyAllWindows()


def canny(arq):
    cap = cv2.imread(arq)
    cv2.namedWindow('Canny')
    canny = cv2.Canny(cap, 100, 200)
    cv2.createTrackbar('Min', 'Canny', 1, 1000, nothing)
    cv2.createTrackbar('Max', 'Canny',1, 1000, nothing)
    while True:
        cv2.imshow('Canny', canny)
        k = cv2.waitKey(1)
        if k == 27:
            cv2.imwrite('canny.jpg', canny)
            break
        min = cv2.getTrackbarPos('Min', 'Canny')
        max = cv2.getTrackbarPos('Max', 'Canny')
        canny = cv2.Canny(cap, min, max)
    cv2.destroyAllWindows()
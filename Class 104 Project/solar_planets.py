import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
            "Sun",
            (20, 300),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            2,
            (255,225,225))

cv2.putText(img,
            "Mercury",
            (125, 190),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,225,225))

cv2.putText(img,
            "Venus",
            (197, 250),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,225,225))

cv2.putText(img,
            "Earth",
            (285, 175),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,225,225))

cv2.putText(img,
            "Mars",
            (390, 250),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,225,225))

cv2.putText(img,
            "Jupiter",
            (590, 50),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,225,225))

cv2.putText(img,
            "Saturn",
            (775, 300),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,225,225))

cv2.putText(img,
            "Uranus",
            (970, 140),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,225,225))

cv2.putText(img,
            "Neptune",
            (1115, 140),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,225,225))

cv2.imshow("output", img)

cv2.waitKey(0)
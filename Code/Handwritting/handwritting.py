import pywhatkit as kit
import cv2

kit.text_to_handwriting("Hi this is Aditya",save_to="hey aditya.png")
img = cv2.imread("hey aditya.png")
cv2.imshow("Hit",img)
cv2.waitKey(0)
cv2.destoryAllWindows()
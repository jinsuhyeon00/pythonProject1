import cv2

img_source = "trump.jpg"

img = cv2.imread(img_source)

cv2.imshow('OMG',img)
cv2.waitKey()
cv2.destroyAllWindows()
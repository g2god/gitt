import cv2
import numpy as np
img=cv2.imread(r"php4.jpg",1)
image=cv2.resize(img,(300,300))

start_point = (50, 50)
end_point = (250, 250)

color = (250, 0, 0)  

thickness = 4

cv2.line(image, start_point, end_point, color, thickness)

cv2.imshow('Line Drawing', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

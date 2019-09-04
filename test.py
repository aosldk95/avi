import cv2
image = cv2.imread("E:/work/DJI_0014.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("good", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
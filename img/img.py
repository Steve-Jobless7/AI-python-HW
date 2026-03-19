import cv2
image=cv2.imread('example.jpg')
resized_image = cv2.resize(image, (224,224))
cv2.imshow('Processed Image', resized_image)
cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image',800,500)

key = cv2.waitKey(0)

if key==ord('s'):
    cv2.imwrite('grayscale_resized_image.jpg')
else:
    print("Image not saved")
cv2.destroyAllWindows()
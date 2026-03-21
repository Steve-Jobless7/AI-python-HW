import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('example.jpg')


(h,w)=image.shape[:2]
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,45, 1.0)
rotated=cv2.warpAffine(image,M,(w,h))
rotated_rgb=cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8")* 50
brighter=cv2.add(image,brightness_matrix)
brighter_rgb=cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Bright Image")
plt.show()

cropped_image=image[70:120,50:120]
cropped_image=cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image)

plt.title("Cropped Image")
plt.show()

key = cv2.waitKey(0)

if key==ord('s'):
    cv2.imwrite('grayscale_resized_image.jpg')
else:
    print("Image not saved")
cv2.destroyAllWindows()

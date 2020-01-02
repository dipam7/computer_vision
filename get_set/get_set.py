from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# stored as BGR and not RGB
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b,g,r) = image[0][0]
print(f"Pixel at (0,0) Red: {r}, Green: {g} and Blue: {b} ")

image[0][0] = (0, 0, 255)

(b,g,r) = image[0][0]
print(f"Pixel at (0,0) Red: {r}, Green: {g} and Blue: {b} ")

corner = image[0:300, 0:300]
cv2.imshow("Corner", corner)

image[0:300, 0:300] = (0,0,0)
cv2.imshow("Updated", image)

cv2.waitKey(0)
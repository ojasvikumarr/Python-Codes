import cv2 

# Read the image

img = cv2.imread("Week08/lena.jpg")

# preparation for CLAHE

clahe =cv2.createCLAHE()

# Convert to gray scaled img 

gray_img = cv2.cvtColor(img , cv2.COLOR_BRG2GRAY)

# Apply Enchancement

enchanced_img = clahe.apply(gray_img)

# Save it to the File

cv2.imwrite("Week08/enchanced_img.jpg" , enchanced_img)

print("Done Enchancement")
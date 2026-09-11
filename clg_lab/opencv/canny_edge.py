import cv2
import numpy as np

# Read image
img = cv2.imread("clg_lab/opencv/image1.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny Edge Detection
edges = cv2.Canny(blur, 50, 150)

# Morphological Operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Close gaps
morph = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Dilate
morph = cv2.dilate(morph, kernel, iterations=1)

# Find contours
contours, _ = cv2.findContours(
    morph,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Create mask
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Draw contours
cv2.drawContours(
    mask,
    contours,
    -1,
    255,
    cv2.FILLED
)

# Segment object
segmented = cv2.bitwise_and(img, img, mask=mask)

# -------------------------------
# Resize all images to same size
# -------------------------------

width = 600
height = 400

img = cv2.resize(img, (width, height))
edges = cv2.resize(edges, (width, height))
morph = cv2.resize(morph, (width, height))
segmented = cv2.resize(segmented, (width, height))

# Create windows
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Canny Edges", cv2.WINDOW_NORMAL)
cv2.namedWindow("Morphological", cv2.WINDOW_NORMAL)
cv2.namedWindow("Segmented Object", cv2.WINDOW_NORMAL)

# Set same window size
cv2.resizeWindow("Original", width, height)
cv2.resizeWindow("Canny Edges", width, height)
cv2.resizeWindow("Morphological", width, height)
cv2.resizeWindow("Segmented Object", width, height)

# Display
cv2.imshow("Original", img)
cv2.imshow("Canny Edges", edges)
cv2.imshow("Morphological", morph)
cv2.imshow("Segmented Object", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Read in the image
image = cv2.imread('child_2.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Divide the image into a grid of blocks
rows, cols = gray_image.shape
block_rows = rows // 10
block_cols = cols // 10
blocks = [gray_image[r:r+block_rows, c:c+block_cols] for r in range(0, rows, block_rows) for c in range(0, cols, block_cols)]

# Merge blocks that are similar
threshold = 10
merged_blocks = []
for block in blocks:
    mean = np.mean(block)
    std = np.std(block)
    if std < threshold:
        merged_blocks[-1] = cv2.add(merged_blocks[-1], block)
    else:
        merged_blocks.append(block)

# Reconstruct the image from the merged blocks
segmented_image = np.zeros_like(gray_image)
for i, block in enumerate(merged_blocks):
    r = i // 10 * block_rows
    c = i % 10 * block_cols
    segmented_image[r:r+block_rows, c:c+block_cols] = block

# Save the segmented image
cv2.imwrite('segmented_image.png', segmented_image)
cv2.imshow('segmented_image',segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

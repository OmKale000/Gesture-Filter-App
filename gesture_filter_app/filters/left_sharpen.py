import cv2
import numpy as np

def apply_filter(img):
    """Apply sharpening filter."""
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    sharpened = cv2.filter2D(img, -1, kernel)
    return sharpened

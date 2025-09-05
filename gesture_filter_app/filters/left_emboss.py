import cv2
import numpy as np

def apply_filter(img):
    """Apply emboss filter."""
    kernel = np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ])
    embossed = cv2.filter2D(img, -1, kernel) + 128
    return cv2.convertScaleAbs(embossed)

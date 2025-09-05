import cv2
import numpy as np

def apply_filter(img):
    """Apply sepia tone filter to the input image."""
    # Create sepia filter kernel
    kernel = np.array(
        [[0.393, 0.769, 0.189],
         [0.349, 0.686, 0.168],
         [0.272, 0.534, 0.131]]
    )

    sepia_img = cv2.transform(img, kernel)
    sepia_img = np.clip(sepia_img, 0, 255).astype('uint8')
    return sepia_img

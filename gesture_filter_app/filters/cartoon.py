import cv2
import numpy as np

def apply_filter(img):
    """Apply cartoon effect filter to the input image."""
    # Convert to gray and apply median blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)

    # Detect edges using adaptive threshold
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2
    )

    # Apply bilateral filter to smooth colors
    color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)

    # Combine edges and color
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

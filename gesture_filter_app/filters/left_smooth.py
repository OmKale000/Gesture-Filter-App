import cv2

def apply_filter(img):
    """Apply smoothing filter with bilateral filter."""
    return cv2.bilateralFilter(img, d=15, sigmaColor=75, sigmaSpace=75)

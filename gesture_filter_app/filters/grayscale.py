import cv2

def apply_filter(img):
    """Apply grayscale filter to the input image."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

import cv2

def apply_filter(img):
    """Apply negative/inverted colors filter to the input image."""
    negative = cv2.bitwise_not(img)
    return negative

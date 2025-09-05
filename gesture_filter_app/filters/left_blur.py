import cv2

def apply_filter(img):
    """Apply stronger/more intense blur filter."""
    return cv2.GaussianBlur(img, (21, 21), 0)  # Higher kernel for more blur

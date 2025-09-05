import cv2

def apply_filter(img):
    """Apply blur (pixelation) filter to the input image."""
    # Downscale and upscale to pixelate
    height, width = img.shape[:2]
    pixel_size = 15  # Controls pixelation block size

    # Resize to small size and back to original size
    small_img = cv2.resize(img, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_LINEAR)
    pixelated = cv2.resize(small_img, (width, height), interpolation=cv2.INTER_NEAREST)
    return pixelated

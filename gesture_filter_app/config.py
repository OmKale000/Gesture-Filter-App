# Configuration settings common across the project

# List of available filters by their string keys
FILTERS = {
    1: "grayscale",
    2: "cartoon",
    3: "negative",
    4: "sepia",
    5: "blur"
}

# Camera source index (default 0 for primary webcam)
CAMERA_SOURCE = 0

# Frame width and height (optional for resizing)
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# MediaPipe Hands configuration
HAND_TRACKING_MAX_NUM_HANDS = 2
HAND_DETECTION_CONFIDENCE = 0.7
HAND_TRACKING_CONFIDENCE = 0.5

# UI parameters
BUTTON_SIZE = (60, 60)  # Width, height in pixels
BUTTON_MARGIN = 10  # Space between buttons in UI

# Debug or verbose mode
DEBUG = False

BUTTON_RADIUS = 30         # Radius for round filter buttons
BUTTON_SPACING = 20        # Vertical spacing between buttons
BUTTON_AREA_HEIGHT = 300   # Height of the area reserved for buttons
BUTTON_AREA_WIDTH = 200    # Width of the area reserved for buttons


# (Optional) Filter names for UI or debugging
LEFT_FILTER_NAMES = {
    1: "Left Blur",
    2: "Left Edges",
    3: "Left Emboss",
    4: "Left Sharpen",
    5: "Left Smooth",
}

RIGHT_FILTER_NAMES = {
    1: "Grayscale",
    2: "Cartoon",
    3: "Negative",
    4: "Sepia",
    5: "Blur",
}

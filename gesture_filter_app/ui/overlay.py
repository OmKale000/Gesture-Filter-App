import cv2

def draw_roi_rectangle(frame, top_left, bottom_right, active=True):
    """Draws the ROI rectangle on the frame."""
    color = (0, 255, 0) if active else (0, 0, 255)
    thickness = 2 if active else 1
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)


def draw_status_text(frame, text, position=(10, 30)):
    """Draws status text on the frame."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    color = (255, 255, 255)
    thickness = 2
    cv2.putText(frame, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

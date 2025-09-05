import cv2
from gesture_filter_app.config import BUTTON_RADIUS, BUTTON_SPACING, LEFT_FILTER_NAMES, RIGHT_FILTER_NAMES

left_button_positions = []
right_button_positions = []
original_buttons = {}

def initialize_button_positions(frame):
    global left_button_positions, right_button_positions, original_buttons
    frame_height, frame_width = frame.shape[:2]

    left_button_positions.clear()
    right_button_positions.clear()

    ox_left = BUTTON_RADIUS + 20
    oy_left = frame_height - 20 - BUTTON_RADIUS
    original_buttons['left'] = (ox_left, oy_left, BUTTON_RADIUS)

    ox_right = frame_width - 20 - BUTTON_RADIUS
    oy_right = frame_height - 20 - BUTTON_RADIUS
    original_buttons['right'] = (ox_right, oy_right, BUTTON_RADIUS)

    start_x_left = ox_left
    start_y_left = oy_left - (BUTTON_RADIUS * 2 + BUTTON_SPACING)
    for i in range(5):
        cx = start_x_left
        cy = start_y_left - i * (2 * BUTTON_RADIUS + BUTTON_SPACING)
        left_button_positions.append((cx, cy, BUTTON_RADIUS))

    start_x_right = ox_right
    start_y_right = oy_right - (BUTTON_RADIUS * 2 + BUTTON_SPACING)
    for i in range(5):
        cx = start_x_right
        cy = start_y_right - i * (2 * BUTTON_RADIUS + BUTTON_SPACING)
        right_button_positions.append((cx, cy, BUTTON_RADIUS))

def draw_circle_button(frame, center, radius, label, is_active):
    color_fill = (50, 50, 50)
    color_outline = (0, 165, 255) if is_active else (255, 255, 255)
    cv2.circle(frame, center, radius, color_fill, -1)
    cv2.circle(frame, center, radius, color_outline, 3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.75
    thickness = 2
    text_size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    text_pos = (center[0] - text_size[0] // 2, center[1] + text_size[1] // 2)
    cv2.putText(frame, label, text_pos, font, font_scale, (255, 255, 255), thickness)

def draw_filter_buttons(frame, left_selected, right_selected):
    if not left_button_positions or not right_button_positions or not original_buttons:
        initialize_button_positions(frame)

    draw_circle_button(frame, original_buttons['left'][:2], BUTTON_RADIUS, "Orig", left_selected is None)
    draw_circle_button(frame, original_buttons['right'][:2], BUTTON_RADIUS, "Orig", right_selected is None)

    for i, (cx, cy, r) in enumerate(left_button_positions, start=1):
        is_active = (left_selected == i)
        label = f"L{i}"
        draw_circle_button(frame, (cx, cy), r, label, is_active)

    for i, (cx, cy, r) in enumerate(right_button_positions, start=1):
        is_active = (right_selected == i)
        label = f"R{i}"
        draw_circle_button(frame, (cx, cy), r, label, is_active)

def point_in_circle(point, circle_center, radius):
    x, y = point
    cx, cy = circle_center
    return (x - cx) ** 2 + (y - cy) ** 2 <= radius ** 2

def get_pressed_button(fingertip_pos):
    if not left_button_positions or not right_button_positions or not original_buttons:
        return None

    if point_in_circle(fingertip_pos, original_buttons['left'][:2], original_buttons['left'][2]):
        return ('left', 0)
    if point_in_circle(fingertip_pos, original_buttons['right'][:2], original_buttons['right'][2]):
        return ('right', 0)

    for i, (cx, cy, r) in enumerate(left_button_positions, start=1):
        if point_in_circle(fingertip_pos, (cx, cy), r):
            return ('left', i)

    for i, (cx, cy, r) in enumerate(right_button_positions, start=1):
        if point_in_circle(fingertip_pos, (cx, cy), r):
            return ('right', i)

    return None

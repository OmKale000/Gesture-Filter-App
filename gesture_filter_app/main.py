import cv2
import numpy as np
import traceback
from gesture_filter_app.config import (
    CAMERA_SOURCE,
    HAND_TRACKING_MAX_NUM_HANDS,
    HAND_DETECTION_CONFIDENCE,
    HAND_TRACKING_CONFIDENCE,
    DEBUG,
)
from gesture_filter_app.hand_tracking.tracker import HandTracker
from gesture_filter_app.filters import (
    grayscale_filter,
    cartoon_filter,
    negative_filter,
    sepia_filter,
    blur_filter,
    left_blur_filter,
    left_edges_filter,
    left_emboss_filter,
    left_sharpen_filter,
    left_smooth_filter,
)
from gesture_filter_app.ui.buttons import draw_filter_buttons, get_pressed_button
from gesture_filter_app.ui.overlay import draw_status_text

RIGHT_FILTER_FUNCTIONS = {
    1: grayscale_filter,
    2: cartoon_filter,
    3: negative_filter,
    4: sepia_filter,
    5: blur_filter,
}

LEFT_FILTER_FUNCTIONS = {
    1: left_blur_filter,
    2: left_edges_filter,
    3: left_emboss_filter,
    4: left_sharpen_filter,
    5: left_smooth_filter,
}

def main():
    cap = cv2.VideoCapture(CAMERA_SOURCE)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    hand_tracker = HandTracker(
        max_num_hands=HAND_TRACKING_MAX_NUM_HANDS,
        detection_confidence=HAND_DETECTION_CONFIDENCE,
        tracking_confidence=HAND_TRACKING_CONFIDENCE,
    )

    left_selected_filter = None
    right_selected_filter = None

    window_name = "Gesture Controlled ROI Filter"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1280, 720)

    while True:
        try:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame from camera.")
                break

            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (1280, 720))

            hands_landmarks = hand_tracker.find_hands(frame, draw_landmarks=DEBUG)

            if len(hands_landmarks) >= 1:
                hand = hands_landmarks[0]
                def get_pixel_coordinates(hand, lm_id):
                    h, w, _ = frame.shape
                    lm = hand[lm_id]
                    return int(lm.x * w), int(lm.y * h)

                index_finger = get_pixel_coordinates(hand, 8)
                pressed = get_pressed_button(index_finger)
                if pressed is not None:
                    side, fid = pressed
                    if side == 'left':
                        left_selected_filter = fid if fid != 0 else None
                    else:
                        right_selected_filter = fid if fid != 0 else None

            if len(hands_landmarks) == 2:
                left_hand = hands_landmarks[0]
                right_hand = hands_landmarks[1]

                def get_pixel_coordinates(hand, lm_id):
                    h, w, _ = frame.shape
                    lm = hand[lm_id]
                    return int(lm.x * w), int(lm.y * h)

                left_index = get_pixel_coordinates(left_hand, 8)
                left_thumb = get_pixel_coordinates(left_hand, 4)
                right_index = get_pixel_coordinates(right_hand, 8)
                right_thumb = get_pixel_coordinates(right_hand, 4)

                points = np.array([left_thumb, right_thumb, right_index, left_index])

                if points.shape[0] == 4 and cv2.isContourConvex(points) and cv2.contourArea(points) > 1000:
                    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
                    cv2.fillPoly(mask, [points], 255)

                    x, y, w, h = cv2.boundingRect(points)
                    if w > 0 and h > 0:
                        roi = frame[y:y+h, x:x+w]

                        if roi.size == 0:
                            draw_status_text(frame, "Empty ROI, move hands...")
                        else:
                            temp_roi = roi.copy()

                            if left_selected_filter is not None:
                                temp_roi = LEFT_FILTER_FUNCTIONS[left_selected_filter](temp_roi)

                            if right_selected_filter is not None:
                                temp_roi = RIGHT_FILTER_FUNCTIONS[right_selected_filter](temp_roi)

                            roi_mask = mask[y:y+h, x:x+w]
                            original_roi = frame[y:y+h, x:x+w]
                            alpha = 0.7
                            filtered_area = cv2.addWeighted(temp_roi, alpha, original_roi, 1 - alpha, 0)
                            original_roi[roi_mask == 255] = filtered_area[roi_mask == 255]

                        cv2.polylines(frame, [points], isClosed=True, color=(0, 255, 0), thickness=2)
                        draw_status_text(frame, "Tracking (both hands)")
                    else:
                        draw_status_text(frame, "Invalid ROI bounds, adjust hands...")
                        cv2.polylines(frame, [points], isClosed=True, color=(0, 0, 255), thickness=2)
                else:
                    draw_status_text(frame, "Waiting for valid gesture area...")
                    cv2.polylines(frame, [points], isClosed=True, color=(0, 0, 255), thickness=2)
            else:
                draw_status_text(frame, "Waiting for both hands...")

            draw_filter_buttons(frame, left_selected_filter, right_selected_filter)

            cv2.imshow(window_name, frame)

            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord('q')):
                break

        except Exception as e:
            print("Exception in main loop:", e)
            traceback.print_exc()
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

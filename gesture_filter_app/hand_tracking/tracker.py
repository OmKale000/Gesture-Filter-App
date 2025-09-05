import cv2
import mediapipe as mp

# rest of the code...


class HandTracker:
    def __init__(self, max_num_hands=2, detection_confidence=0.7, tracking_confidence=0.5):
        self.max_num_hands = max_num_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=self.max_num_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence,
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, image, draw_landmarks=False):
        """
        Detect hands and return list of landmark lists.
        Each hand landmarks is a list of 21 normalized (x,y,z) landmarks.

        Args:
          image: BGR image from OpenCV.
          draw_landmarks: if True, draw landmarks on the image.

        Returns:
          List of hands landmarks, each is a list of landmarks.
        """
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)

        all_hands_landmarks = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if draw_landmarks:
                    self.mp_draw.draw_landmarks(
                        image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )
                all_hands_landmarks.append(hand_landmarks.landmark)

        return all_hands_landmarks

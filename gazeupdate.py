import cv2
import mediapipe as mp
import numpy as np

def detect_gaze_visual_feedback():
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    # Eye and iris landmark indices
    LEFT_IRIS = [474, 475, 476, 477]
    RIGHT_IRIS = [469, 470, 471, 472]
    LEFT_EYE = [33, 133, 160, 144, 153, 154, 155, 133]
    RIGHT_EYE = [362, 263, 387, 373, 380, 374, 373, 263]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape

                # Get eye and iris landmarks
                left_eye = [(int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h)) for i in LEFT_EYE]
                right_eye = [(int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h)) for i in RIGHT_EYE]
                left_iris = [(int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h)) for i in LEFT_IRIS]
                right_iris = [(int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h)) for i in RIGHT_IRIS]

                # Draw landmarks for visualization
                for point in left_eye + right_eye:
                    cv2.circle(frame, point, 1, (0, 255, 0), -1)
                for point in left_iris + right_iris:
                    cv2.circle(frame, point, 1, (0, 0, 255), -1)

                # Calculate iris center for both eyes
                left_iris_center = np.mean(left_iris, axis=0).astype(int)
                right_iris_center = np.mean(right_iris, axis=0).astype(int)

                # Find the average iris center (for both eyes)
                combined_iris_center = np.mean([left_iris_center, right_iris_center], axis=0).astype(int)

                # Draw a circle at the iris center for visualization
                cv2.circle(frame, tuple(combined_iris_center), 5, (0, 255, 255), -1)

        cv2.imshow('Gaze Visualization', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_gaze_visual_feedback()

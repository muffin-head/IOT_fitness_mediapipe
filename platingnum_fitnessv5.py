from mediapipe import solutions
import cv2
import numpy as np

def map_to_grid(x, grid_width, frame_width):
    grid_number = int(x * frame_width / grid_width)
    grid_x = grid_width * grid_number + grid_width / 2
    return grid_x

def draw_landmarks_and_grid(frame, pose_landmarks, grid_width, grid_centers):
    annotated_frame = frame.copy()
    for i in range(0, frame.shape[1], grid_width):
        cv2.line(annotated_frame, (i, 0), (i, frame.shape[0]), (255, 0, 0), 1)
    for i in range(1, len(grid_centers)):
        cv2.line(annotated_frame, grid_centers[i - 1], grid_centers[i], (0, 255, 255), 2)
    for landmark in pose_landmarks:
        x = int(landmark.x * frame.shape[1])
        y = int(landmark.y * frame.shape[0])
        cv2.circle(annotated_frame, (x, y), 5, (0, 255, 0), -1)
    return annotated_frame

def extract_feet_pose(video_path, grid_width=100, frame_skip_rate=2, max_distance=170, visibility_threshold=0.3):
    pose = solutions.pose.Pose(static_image_mode=False, model_complexity=0)
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter('annotated_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    last_valid_center = None  # Store the last valid center
    grid_centers = []

    while cap.isOpened():
        for _ in range(frame_skip_rate - 1):
            cap.read()
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        if results.pose_landmarks:
            left_foot_landmark = results.pose_landmarks.landmark[29]
            if left_foot_landmark.visibility > visibility_threshold:
                left_grid_x = map_to_grid(left_foot_landmark.x, grid_width, width)
                left_grid_y = int(left_foot_landmark.y * height)
                grid_center = (int(left_grid_x), left_grid_y)

                if last_valid_center is None or np.linalg.norm(np.array(last_valid_center) - np.array(grid_center)) <= max_distance:
                    grid_centers.append(grid_center)
                    last_valid_center = grid_center

            annotated_frame = draw_landmarks_and_grid(frame, [left_foot_landmark], grid_width, grid_centers)
            out.write(annotated_frame)
            cv2.imshow('Annotated Frame', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

video_path = 'C:\\Users\\c23005186\\Downloads\\Telegram Desktop\\tennis.mp4'
extract_feet_pose(video_path, grid_width=100, frame_skip_rate=2)

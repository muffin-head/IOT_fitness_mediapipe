import cv2
from mediapipe import solutions
import numpy as np

def extract_and_visualize_feet_pose(video_path):
    pose = solutions.pose.Pose(static_image_mode=False, model_complexity=2)
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    cv2.namedWindow('Video and Visualization', cv2.WINDOW_NORMAL)
    
    height_measurements = []  # To collect height data
    fallback_height = 1  # Fallback to avoid division by zero, adjust based on expected height scale

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process the frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)
        
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            
            # Calculate the height of the person in the frame
            current_height = calculate_person_height(landmarks, frame)
            if current_height > 0:  # Validate height to ensure it's reasonable
                height_measurements.append(current_height)
            
            average_height = np.mean(height_measurements) if height_measurements else fallback_height
            
            left_foot = landmarks[15]  # Left foot landmark index
            # Normalize coordinates based on average height for scaling
            x = (left_foot.x * frame.shape[1]) / average_height
            y = (left_foot.y * frame.shape[0]) / average_height
            
            vis = np.zeros((500, 500, 3), dtype=np.uint8)  # Visualization canvas
            cv2.circle(vis, (int(x * 100), int(y * 100)), 10, (0, 255, 0), -1)  # Scale for visibility
            
            # Show original frame
            frame_resized = cv2.resize(frame, (500, 500))
            combined = np.hstack((frame_resized, vis))
            cv2.imshow('Video and Visualization', combined)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def calculate_person_height(landmarks, frame):
    head_index = 0  # Index for head top in MediaPipe
    foot_index = 29  # Index for foot in MediaPipe
    head = landmarks[head_index]
    foot = landmarks[foot_index]
    # Pixel height calculation
    return abs(head.y - foot.y) * frame.shape[0]

# Path to your video
video_path = 'C:\\Users\\c23005186\\Downloads\\Telegram Desktop\\tennis.mp4'
extract_and_visualize_feet_pose(video_path)

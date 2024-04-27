from mediapipe import solutions
import cv2

# Function to extract feet pose from each frame of the video
def extract_feet_pose(video_path):
    # Load MediaPipe Pose model
    pose = solutions.pose.Pose(static_image_mode=False, model_complexity=0)

    # Open video file
    cap = cv2.VideoCapture(video_path)

    # Check if video file opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Create VideoWriter object to save annotated video
    out = cv2.VideoWriter('annotated_video.mp4', 
                          cv2.VideoWriter_fourcc(*'mp4v'), 
                          fps, 
                          (width, height))

    # Process each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame to get pose landmarks
        results = pose.process(rgb_frame)

        # Extract landmarks for feet (index 11 and 12 for left and right feet respectively)
        if results.pose_landmarks:
            left_foot_landmark = results.pose_landmarks.landmark[29]
            right_foot_landmark = results.pose_landmarks.landmark[30]

            # Print coordinates of left and right feet
            print("Left Foot Pose:", left_foot_landmark)
            print("Right Foot Pose:", right_foot_landmark)

            # Visualize the pose landmarks on the frame
            annotated_frame = draw_landmarks(frame, [left_foot_landmark, right_foot_landmark])

            # Write annotated frame to output video
            out.write(annotated_frame)

            # Display the annotated frame
            cv2.imshow('Annotated Frame', annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Function to draw landmarks on a frame
def draw_landmarks(frame, pose_landmarks):
    # Draw landmarks on the frame
    annotated_frame = frame.copy()
    for landmark in pose_landmarks:
        x = int(landmark.x * frame.shape[1])
        y = int(landmark.y * frame.shape[0])
        cv2.circle(annotated_frame, (x, y), 5, (0, 255, 0), -1)
    return annotated_frame

# Process the video and extract feet pose in real-time
video_path = 'C:\\Users\\c23005186\\Downloads\\Telegram Desktop\\tennis.mp4'
extract_feet_pose(video_path)

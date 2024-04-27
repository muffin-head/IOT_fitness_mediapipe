from mediapipe import solutions
import cv2

# Function to map x coordinate to grid coordinates
def map_to_grid(x, grid_width, frame_width):
    grid_number = int(x * frame_width / grid_width)
    grid_x = grid_width * grid_number + grid_width / 2
    return grid_x

# Function to draw landmarks and grids on a frame
def draw_landmarks_and_grid(frame, pose_landmarks, grid_width):
    # Draw landmarks on the frame
    annotated_frame = frame.copy()

    # Draw grid lines on the frame
    for i in range(0, frame.shape[1], grid_width):
        cv2.line(annotated_frame, (i, 0), (i, frame.shape[0]), (255, 0, 0), 1)

    # Draw landmarks
    for landmark in pose_landmarks:
        x = int(landmark.x * frame.shape[1])
        y = int(landmark.y * frame.shape[0])
        cv2.circle(annotated_frame, (x, y), 5, (0, 255, 0), -1)
    
    return annotated_frame

# Function to extract feet pose from each frame of the video
def extract_feet_pose(video_path, grid_width=100):  # Grid width can be adjusted
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

    # Variables to track previous grid x-coordinates
    last_left_grid_x = -1
    last_right_grid_x = -1

    # Process each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame to get pose landmarks
        results = pose.process(rgb_frame)

        # Extract landmarks for feet
        if results.pose_landmarks:
            left_foot_landmark = results.pose_landmarks.landmark[29]
            right_foot_landmark = results.pose_landmarks.landmark[30]

            # Calculate grid-based x-coordinate
            left_grid_x = map_to_grid(left_foot_landmark.x, grid_width, width)
            right_grid_x = map_to_grid(right_foot_landmark.x, grid_width, width)

            # Check if feet moved to a new grid
            if left_grid_x != last_left_grid_x or right_grid_x != last_right_grid_x:
                print(f"New Left Foot Coordinates: ({left_grid_x}, {left_foot_landmark.y * height})")
                print(f"New Right Foot Coordinates: ({right_grid_x}, {right_foot_landmark.y * height})")
                last_left_grid_x, last_right_grid_x = left_grid_x, right_grid_x

            # Visualize the pose landmarks and grid on the frame
            annotated_frame = draw_landmarks_and_grid(frame, [left_foot_landmark, right_foot_landmark], grid_width)

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

# Process the video and extract feet pose in real-time
video_path = 'C:\\Users\\c23005186\\Downloads\\Telegram Desktop\\tennis.mp4'
extract_feet_pose(video_path, grid_width=100)  # Grid width set to 100 pixels

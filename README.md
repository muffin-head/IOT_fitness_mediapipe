
# Feet Position Tracker

## Project Overview
This project is designed to analyze videos of workouts to track the movement of feet using a grid-based system. It utilizes the MediaPipe framework for pose detection and OpenCV for video processing. The output is an annotated video that shows the grid system and foot positions, along with console output whenever the feet move to a different grid cell on the x-axis.

## Requirements
- Python 3.7 or higher
- OpenCV
- MediaPipe

## Installation
To run this project, you need to install the required Python libraries. You can install these libraries using `pip`. Execute the following command in your terminal:

```bash
pip install opencv-python mediapipe
```

## Usage
To use this script, follow these steps:
1. Ensure you have a video file ready for analysis.
2. Edit the `video_path` variable in the script to point to the location of your video file.
3. Optionally, adjust the `grid_width` parameter in the `extract_feet_pose` function call to change the sensitivity of the grid system.
4. Run the script using Python:

```bash
python feet_position_tracker.py
```

During execution, press 'q' to quit the video playback window.

## Output
The script processes the video and provides two forms of output:
1. **Annotated Video**: The output video will display the grid system and the positions of the left and right feet marked on each frame.
2. **Console Output**: Whenever the feet change to a different grid cell along the x-axis, the new coordinates of the feet will be printed in the console.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

## License
Specify your license or if the project is open-source, you might use the MIT License or any other open-source license.

## Contact
For questions and feedback, please open an issue in the GitHub repository or contact the repository owner directly.
```

### Notes:
- Make sure to replace placeholders like the contact information or the licensing details with actual data.
- If there are any specific conventions or additional features in your project, consider adding sections such as **Configurations** for any setup details, or **Limitations** to outline any known issues with the current implementation.
- Encourage community engagement by providing a clear **Contributing** section, as included.
- The installation instructions assume that `pip` is available. If your environment or target users typically use a different package manager (like `conda`), adjust the instructions accordingly.
- Lastly, it's good practice to link to official documentation for key dependencies like OpenCV and MediaPipe for users who might need more detailed setup instructions or troubleshooting.```

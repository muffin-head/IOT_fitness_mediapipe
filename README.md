

# Movement Pattern Tracker

## Project Overview
This project analyzes side-view videos to project movements onto a simulated Z-axis, focusing on the stability and pattern of movements using a grid-based system. It utilizes the MediaPipe framework for pose detection and OpenCV for video processing, with an emphasis on tracking more stable markers (e.g., hips) instead of feet for greater accuracy. The output is an annotated video that shows the grid system and movement paths, providing insights into how a person moves and their movement patterns.

## Requirements
- Python 3.7 or higher
- OpenCV
- MediaPipe

## Installation
Install the required Python libraries using `pip`. Run the following command in your terminal:

```bash
pip install opencv-python mediapipe
```

## Usage
To use this script, follow these steps:
1. Have a side-view video file ready for analysis.
2. Set the `video_path` variable in the script to your video file location.
3. Adjust `grid_size` and `frame_skip_rate` in the `extract_and_visualize_feet_pose` function to modify grid sensitivity and processing speed.
4. Execute the script with Python:

```bash
python platingnum_fitnessv6.py
```

Press 'q' during execution to quit the video playback window.

## Output
The script processes the video and provides:
1. **Annotated Video**: Displays the grid system with markers representing the movement of the hips. Paths connecting sequential positions indicate movement patterns and stability.
2. **Console Output**: Whenever the marker changes to a different grid cell on the x-axis, the new coordinates are printed to the console.

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request with your enhancements.

## License
This project is open-source under the MIT License. See the LICENSE file in the repository for more details.

## Contact
For questions and feedback, please open an issue in the GitHub repository or contact the repository owner directly.

### Notes:
- Installation instructions assume the availability of `pip`. Adjust these instructions if your environment uses a different package manager like `conda`.
- For detailed setup instructions or troubleshooting, consider linking to the official documentation for dependencies like OpenCV and MediaPipe.

---

This revised README better matches the current functionality of your project, highlighting the changes in tracking strategy and the methodological shift to a focus on aggregate movement patterns and stability, which is more suitable for side-view video analysis.

# Gaze Detection with Visual Feedback

This project is a Python-based implementation of gaze detection using Mediapipe's Face Mesh solution. The program detects and tracks the position of the eyes and irises in real-time using a webcam, providing visual feedback by overlaying markers on the video feed.

## Features
- Real-time detection of facial landmarks using Mediapipe's Face Mesh.
- Identification of eye and iris positions.
- Visual feedback with circles drawn around eye and iris landmarks.
- Visualization of the average iris center for both eyes.

## Requirements

To run this project, you need the following:

- Python 3.7 or higher
- OpenCV
- Mediapipe
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gaze-detection.git
   cd gaze-detection
   ```

2. Install the required dependencies:
   ```bash
   pip install opencv-python mediapipe numpy
   ```

## Usage

1. Run the Python script:
   ```bash
   python detect_gaze_visual_feedback.py
   ```

2. Allow access to your webcam.

3. The program will display a window showing the live webcam feed with the following visual feedback:
   - Green circles: Eye landmarks
   - Red circles: Iris landmarks
   - Yellow circle: Combined center of the left and right irises

4. Press the `q` key to exit the program.

## Code Overview

The main script (`detect_gaze_visual_feedback.py`) includes the following components:

- **Initialization**: Setting up Mediapipe Face Mesh and OpenCV.
- **Eye and Iris Landmark Detection**: Extracting facial landmarks corresponding to the eyes and irises.
- **Visual Feedback**: Drawing circles on eye and iris landmarks, and calculating the average iris center.
- **Webcam Loop**: Continuously processing frames from the webcam and displaying visual feedback.



## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Mediapipe](https://github.com/google/mediapipe) for the Face Mesh solution.
- [OpenCV](https://opencv.org/) for real-time video processing.
- [NumPy](https://numpy.org/) for numerical computations.



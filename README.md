Hi!! This is Jatin Hans.

First of all, thankyou for showing your interest in my project.
Here's the detailed explanation of my project.

# AI Virtual Keyboard

## Overview

The AI Virtual Keyboard is a Python-based project that uses computer vision and hand-tracking technology to simulate a virtual keyboard. Users can interact with the virtual keyboard using their hands, allowing for touchless typing. This project leverages OpenCV, MediaPipe, and Pynput libraries to track hand movements, detect hand landmarks, and simulate keyboard inputs.

## Features

- **Hand Tracking**: Uses MediaPipe to detect and track hand landmarks.
- **Virtual Keyboard**: A graphical representation of a keyboard on the screen.
- **Touchless Typing**: Users can type by moving their hands over the virtual keys.
- **Mouse Interaction**: Allows interaction with the virtual keyboard using a mouse.
- **Keyboard Simulation**: Simulates real keyboard inputs using the Pynput library.

## Requirements

- Python 3.6+
- OpenCV
- MediaPipe
- Pynput

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/aivirtualkeyboard.git
    cd aivirtualkeyboard
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install opencv-python mediapipe pynput
    ```

## Usage

1. Run the main script:
    ```sh
    python virtualkeyboard.py
    ```

2. A window will open showing the video feed from your webcam. The virtual keyboard will be displayed on the screen.

3. Use your hand to interact with the keys on the virtual keyboard. The software tracks your index finger and thumb to detect clicks.

4. You can also use your mouse to interact with the virtual keyboard by clicking on the keys.

5. To exit the application, press the 'q' key on your keyboard.

## File Descriptions

- **virtualkeyboard.py**: The main script that initializes the virtual keyboard, handles video capture, and manages user interactions.
- **handtracking.py**: Contains the `HandTracker` class that uses MediaPipe to detect and track hand landmarks.
- **keys.py**: Contains the `Key` class that defines the properties and methods for the virtual keys.

## HandTracking Class

### `HandTracker`
- **Initialization Parameters**:
  - `mode` (bool): Whether to treat the input images as a batch of static images, or a video stream.
  - `maxHands` (int): Maximum number of hands to detect.
  - `detectionCon` (float): Minimum confidence value ([0.0, 1.0]) for hand detection to be considered successful.
  - `trackCon` (float): Minimum confidence value ([0.0, 1.0]) for the hand landmarks to be considered tracked successfully.

- **Methods**:
  - `findHands(img, draw=True)`: Processes the image to detect hands and optionally draw landmarks.
  - `getPosition(img, handNo=0, draw=True)`: Returns the list of hand landmarks' positions.

## Key Class

### `Key`
- **Initialization Parameters**:
  - `x` (int): X-coordinate of the key.
  - `y` (int): Y-coordinate of the key.
  - `w` (int): Width of the key.
  - `h` (int): Height of the key.
  - `text` (str): The text label of the key.

- **Methods**:
  - `drawKey(img, text_color=(255, 255, 255), bg_color=(0, 0, 0), alpha=0.5, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, thickness=2)`: Draws the key on the given image.
  - `isOver(x, y)`: Checks if a given point (x, y) is over the key.

## Troubleshooting

- Ensure your webcam is properly connected and recognized by the system.
- If the script fails to start, check for any missing dependencies and install them using `pip install -r requirements.txt`.
- If the hand tracking is not accurate, adjust the `detectionCon` and `trackCon` parameters in the `HandTracker` initialization.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [MediaPipe](https://github.com/google/mediapipe) by Google for hand tracking.
- [OpenCV](https://opencv.org/) for computer vision functionalities.
- [Pynput](https://pypi.org/project/pynput/) for keyboard input simulation.

---

Feel free to customize this README file according to your specific needs and repository details.

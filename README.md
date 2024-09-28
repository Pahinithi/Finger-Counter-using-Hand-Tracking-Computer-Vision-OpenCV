# Finger Counter using Hand Tracking | Computer Vision | OpenCV Python

This project is a computer vision-based **finger counter** built using **OpenCV** and a custom **Hand Tracking Module**. The system detects the number of fingers raised in front of the webcam in real time and displays the corresponding finger count image.


## Features

- **Real-time hand detection and finger counting** using a webcam feed.
- Utilizes **OpenCV** for image processing.
- Implements **MediaPipe Hand Tracking** for detecting hand landmarks.
- Displays an image that matches the number of fingers raised.
- Real-time **Frames Per Second (FPS)** calculation for performance monitoring.

## Demo

click here![https://drive.google.com/file/d/1jzWXwkOnrxPtqJcm1tYCfPFqdaVf6lD7/view?usp=sharing)

## Installation

### Prerequisites

Ensure you have Python and the following libraries installed before running the project:

```bash
pip install opencv-python
pip install mediapipe
```

### Clone the Repository

```bash
git clone https://github.com/Pahinithi/Finger-Counter-using-Hand-Tracking-Computer-Vision-OpenCV
cd Finger-Counter-Hand-Tracking
```

### Project Structure

- **`FingerCounter.py`**: Main script that captures the webcam feed, tracks the hand, and counts the raised fingers.
- **`HandTrackingModule.py`**: Module responsible for detecting hands and tracking their key points (landmarks) using **MediaPipe**.
- **`FingerImages/`**: Contains images (0-5 fingers) that are displayed based on the detected finger count.
- **`__pycache__/`**: Cache directory for Python compiled files.

### Running the Application

1. To run the finger counter application, execute:

```bash
python FingerCounter.py
```

2. Ensure your webcam is properly connected. The script will start detecting your hand and counting the number of fingers raised in front of the camera.

3. To exit the application, press `q` while the window is active.

### Folder Structure

```
.
├── FingerCounter.py           # Main file to run the application
├── HandTrackingModule.py      # Hand tracking module
├── FingerImages/              # Folder with images to display for corresponding finger counts
├── __pycache__/               # Compiled Python cache files
```

## How It Works

- The application captures live video feed from your webcam.
- The **HandTrackingModule** detects hand landmarks using **MediaPipe**.
- It analyzes the position of the fingertips relative to key joints to determine whether each finger is raised or not.
  - **Thumb**: A horizontal check is done (left-to-right) based on the position of the thumb's tip and joints.
  - **Other Fingers**: A vertical check (top-to-bottom) is used to identify if fingers are raised, based on the positions of their tips and joints.
  
- Based on the number of raised fingers, the corresponding image from the **FingerImages** folder is displayed on the screen.
- The FPS (Frames Per Second) of the live webcam feed is also displayed to show performance.

## Screenshots


<img width="1728" alt="CV08" src="https://github.com/user-attachments/assets/2f0afab6-7917-42f1-82c7-4e2b1edc6739">


## Technologies Used

- **Python**: Programming language.
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For real-time hand tracking and finger landmark detection.

## Future Improvements

- **Accuracy**: Further fine-tuning to improve the detection of fingers in various lighting conditions.
- **Gesture Recognition**: Adding gesture recognition functionality to detect specific hand movements.
- **UI Enhancements**: Improving the overall user interface for a more interactive experience.

## License

This project is licensed under the MIT License. 


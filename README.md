MediaPipe and OpenCV Demo Collection
This repository contains a collection of Python scripts and notebooks demonstrating the use of MediaPipe, OpenCV, and other computer vision tools for various applications, including face detection, pose estimation, hand tracking, and gesture recognition. It also includes supplementary files, models, and configurations.

Directory Structure
MediaPipe Demos
Face Mesh

DemoMediapipe01_Face_Mesh.py: Demonstrates the use of MediaPipe's Face Mesh model to detect facial landmarks.
Pose Estimation

DemoMediapipe01_Pose.py: Tracks human pose landmarks using MediaPipe Pose.
DemoMediapipe01_Pose_Game.py: A gamified demonstration of pose tracking.
Hand Tracking

DemoMediapipe02_Hands.py: Tracks hand landmarks using MediaPipe Hands.
Face and Hands

DemoMediapipe03_Face_Hands.py: Combines face and hand tracking.
Individual Hand Tracking

DemoMediapipe04_2_Hands_ind.py: Tracks two hands independently.
Games with MediaPipe

DemoMediapipe04_Game0.py: A game demonstration using MediaPipe.
DemoMediapipe05_Game1.py: Game 1 using MediaPipe.
DemoMediapipe05_Game2.py: Game 2 using MediaPipe.
Comprehensive Face, Hands, and Pose

DemoMediapipe06_FaceHandsPose.py: Tracks face, hands, and pose landmarks simultaneously.
Gesture Recognition

DemoMediapipe07_Gesture00.py: Basic gesture recognition demonstration.
DemoMediapipe07_Gesture01.py: Advanced gesture recognition.
Jupyter Notebook Demos
JupyterDemo1.ipynb: Interactive demo showcasing MediaPipe and OpenCV capabilities in a notebook environment.
Untitled.ipynb: Additional notebook (content unspecified, review for relevance).
Pre-Trained Models
MobileNetSSD_deploy.caffemodel: Pre-trained MobileNet-SSD model for object detection.
MobileNetSSD_deploy.prototxt: Configuration file for MobileNet-SSD.
Supplementary MediaPipe Scripts
facedetection.py: Face detection using MediaPipe.
facemeshlandmarksdetection.py: Detects facial landmarks using MediaPipe's Face Mesh.
handsdetection.py: Hand tracking with MediaPipe.
posedetection.py: Pose detection with MediaPipe.
mediapipehelper.py: Helper functions for MediaPipe integration.
OpenCV Demos
Image Processing

opencvDemo0_imread.py: Reads and displays an image using OpenCV.
opencvDemo1_imshow.py: Displays images using OpenCV.
Camera and Video

opencvDemo2_CamSet.py: Captures and configures webcam feed.
opencvDemo3_row_col_win.py: Explores image matrix dimensions.
opencvDemo4_Board.py: Creates a graphical board overlay.
opencvDemo5_putTextFrame.py: Adds text to video frames.
opencvDemo6_putTextImage.py: Adds text to static images.
Object Detection

opencvDemo7_imagePersonDetector.py: Detects people in static images.
opencvDemo8_FrameObjectDetector.py: Object detection in video frames.
opencvDemo9_FrameObjectDet2.py: Extended object detection.
Face and Eye Detection

opencvDemo19_Face_Eyes_Cascade.py: Face and eye detection using Haar cascades.
opencvDemo20_Eyes_Cascade.py: Dedicated eye detection script.
opencvDemo22_Face_Me.py: Face tracking and display.
Interactive Tools

opencvDemo11_FrameROIClick.py: Select regions of interest (ROIs) by clicking.
opencvDemo12_Trackbar.py: Creates a trackbar for dynamic adjustments.
opencvDemo13_TrackbarMoveWindow.py: Moves OpenCV windows interactively.
opencvDemo14_ColorBox.py: Displays color boxes.
opencvDemo15_SatValColor.py: Interactive color manipulation with sliders.
opencvDemo16_SatValHueTrackbar.py: Hue adjustment with trackbars.
opencvDemo17_FrameMask.py: Generates masks for video frames.
opencvDemo18_FrameMaskComposed.py: Combines multiple masks for processing.
Miscellaneous Demos

opencvDemo10.py to opencvDemo26.py: Various demonstrations of OpenCV functionality. Refer to the code comments for specifics.
General Python Scripts
RandomDemo.py: Demonstrates random Python functionality.
TupleDemo.py: Demonstrates tuple operations in Python.
setDemo.py: Illustrates set operations.
Server and Client
server.py: Simple Python server script.
client.py: Client-side implementation.
Resources
requirements.txt: List of Python dependencies.
package-lock.json: Dependency lock file (npm, potentially unused in this context).
train.pkl: Serialized training data for machine learning models.
Media Files
person.jpg: Sample image for testing.
video1.mp4: Sample video for testing.
wind.png: Sample image resource.


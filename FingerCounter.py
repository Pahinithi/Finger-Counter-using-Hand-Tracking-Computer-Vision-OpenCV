import cv2
import time
import os
import HandTrackingModule as htm

# Set webcam resolution
wCam, hCam = 640, 480

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Folder where finger images are stored
folderPath = "FingerImages"

# Check if the folder exists
if not os.path.exists(folderPath):
    print(f"Error: '{folderPath}' directory does not exist.")
    exit()

# Load and resize finger counting images
myList = os.listdir(folderPath)
overlayList = [cv2.resize(cv2.imread(f'{folderPath}/{imPath}'), (wCam, int(hCam * 0.5))) for imPath in myList]

# Check if the images are loaded correctly
print(f"Loaded {len(overlayList)} images for finger counting.")

# Time variables for FPS calculation
pTime = 0

# Hand detector instance
detector = htm.handDetector(detectionCon=0.75)

# IDs for the tips of the fingers (based on landmarks from MediaPipe)
tipIds = [4, 8, 12, 16, 20]

while True:
    # Read frame from webcam
    success, img = cap.read()
    
    if not success:
        print("Error: Unable to read from the camera.")
        break

    # Find the hands and positions
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if lmList:
        fingers = []

        # Thumb (horizontal check)
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Four other fingers (vertical check)
        for i in range(1, 5):
            if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Count the number of raised fingers
        totalFingers = fingers.count(1)
        print(f"Fingers up: {totalFingers}")

        # Display the corresponding finger image
        if 0 < totalFingers <= len(overlayList):
            h, w, _ = overlayList[totalFingers - 1].shape
            img[0:h, 0:w] = overlayList[totalFingers - 1]

        # Draw rectangle and display the number of fingers
        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Show the image
    cv2.imshow("Finger Counter", img)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

# import sys
# sys.path.append('/home/anas/testv/lib/python3.11/site-packages')

from ultralytics import YOLO
import cv2
import math



class YoloModel:
    def __init__(self) :
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Set width to 320
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Set height to 240
        cap.set(cv2.CAP_PROP_FPS, 15)  # Reduce frame rate to 15 FPS
        self.cap=cap
        self.model = YOLO("yolov8n.pt")
        # Object classes
        self.classNames = ["car", "aeroplane"]  # تقليل عدد الفئات


    def detection_object(self,frame):
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        model=self.model
        results = model(frame, stream=True, verbose=False, imgsz=320)
        for r in results:
            boxes = r.boxes

            for box in boxes:
                cls = int(box.cls[0])

                # Check if the detected object is car (0) or aeroplane (1)
                if cls in [0, 1]:
                    # Bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

                    # Draw box on frame
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

                    # Confidence
                    confidence = math.ceil((box.conf[0] * 100)) / 100

                    # Object details
                    org = [x1, y1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 0.5
                    color = (255, 255, 255)
                    thickness = 1

                    cv2.putText(frame, classNames[cls], org, font, fontScale, color, thickness)
        return x1, y1, x2, y2

        
# Start webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Set width to 320
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Set height to 240
cap.set(cv2.CAP_PROP_FPS, 15)  # Reduce frame rate to 15 FPS

model = YOLO("yolov8n.pt")

# Object classes
classNames = ["car", "aeroplane"]  # تقليل عدد الفئات

def detection_object(frame):
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    results = model(frame, stream=True, verbose=False, imgsz=320)
    for r in results:
        boxes = r.boxes

        for box in boxes:
            cls = int(box.cls[0])

            # Check if the detected object is car (0) or aeroplane (1)
            if cls in [0, 1]:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

                # Draw box on frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

                # Confidence
                confidence = math.ceil((box.conf[0] * 100)) / 100

                # Object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 0.5
                color = (255, 255, 255)
                thickness = 1

                cv2.putText(frame, classNames[cls], org, font, fontScale, color, thickness)
    return x1, y1, x2, y2


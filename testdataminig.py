import sys
sys.path.append('/home/anas/testv/lib/python3.11/site-packages')

import torchvision.transforms as T
from torchvision.models.detection import ssdlite320_mobilenet_v3_large
import torch
import cv2
import numpy as np

class_names = [
    "background",
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "dining table",
    "toilet",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush"
]

# Load the model
model = ssdlite320_mobilenet_v3_large(pretrained=True)
model.eval()

# # Define image transformations
# transform = T.Compose([
#     T.ToTensor()
# ])

# # Initialize the video capture
# cap = cv2.VideoCapture(0)

# # Set frame dimensions and FPS
# width = 320  # Reduced frame width
# height = 240  # Reduced frame height
# fps = 15  # Reduced FPS
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# cap.set(cv2.CAP_PROP_FPS, fps)

# # Loop to capture frames from the camera
# while True:
#     # Read a frame from the camera
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert frame to RGB (OpenCV captures frames in BGR format by default)
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Apply transformations
#     frame_tensor = transform(frame_rgb).unsqueeze(0)

#     # Perform inference
#     with torch.no_grad():
#         predictions = model(frame_tensor)

#     # Draw bounding boxes and labels on the frame
#     for score, label, box in zip(predictions[0]['scores'], predictions[0]['labels'], predictions[0]['boxes']):
#         if score > 0.5:
#             # Convert box coordinates to integers
#             box = [int(i.item()) for i in box]

#             # Draw bounding box
#             cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)

#             # Add label text
#             label_text = f"Label: {class_names[label.item()]}"
#             print(label.item())
#             cv2.putText(frame, label_text, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

#     # Display the frame
#     cv2.imshow('Object Detection', frame)

#     # Check for the 'q' key to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all windows
# cap.release()
# cv2.destroyAllWindows()
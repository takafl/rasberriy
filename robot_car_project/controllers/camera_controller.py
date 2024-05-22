import cv2
from models.custom_queue import CustomQueuedata
from controllers.ai_vision_controller import AiVistionController
from models.custom_data_frame import CustomDataframe
class CameraController:
    def __init__(self) :
          self.cap:cv2.VideoCapture = cv2.VideoCapture(0)
          self.q=CustomQueuedata()
          self.helper=AiVistionController()

    def startCamera(self):

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break  # Break the loop if the video is over
            h,w,_=frame.shape
            cv2.rectangle(frame, (w//2, h//2), (w//2, h//2), (0, 0, 255), 3)
            x,y,w,h,center_x,center_y=self.helper.detectionObjectsFromFrame(frame)
            customFrame = CustomDataframe(arry=frame,center_x=center_x,center_y=center_y)
            self.helper.drawRectangle(customFrame)
            self.q.appent2list(customFrame)
            self.helper.handelFrames(customFrame,lambda x:print(f'left {x}'),lambda x:print(f'right {x}'),lambda : print("forward"))

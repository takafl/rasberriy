
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import  math as maths
from models.custom_queue import CustomQueuedata
from models.custom_data_frame import CustomDataframe
from ai_models.yolo_model import YoloModel
class AiVistionController:
    def __init__(self) -> None:
        self.yolo=YoloModel()
    # detection object
    def detectionObjectsFromFrame(self,frame):
        x, y, w, h = self.yolo.detection_object(frame)
        center_x = (x + w )// 2
        center_y = (y + h) // 2
        return x,y,w,h,center_x,center_y
    # function to detection and draw the rectangle

    def detectionObjectsAndDrowRectangleFromFrame(self,frame:CustomDataframe):
        _,_,_,_,center_x,center_y = AiVistionController.detectionObjectsFromFrame(frame)
        AiVistionController.drawRectangle(frame,center_x,center_y)

    # draw rectangle
    def drawRectangle(self,frame:CustomDataframe):
        cv2.rectangle(frame.frame, (frame.center_x, frame.center_y), (frame.center_x, frame.center_y), (0, 0, 255), 3)
        return frame.frame


    def handelFrames(self,frame:CustomDataframe,onLeft,onRight,onForword):
            if maths.fabs(320-frame.center_x)<=20:
               onForword()
            else:
                distans=320-frame.center_x
                if distans<=0:
                        #  directions.append("Right")
                    onRight(maths.fabs(distans))
                else:
                    
                    onLeft(maths.fabs(distans))
           


 





         





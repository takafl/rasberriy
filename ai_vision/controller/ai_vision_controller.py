
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import  yolo
import  math as maths
from ..domain.custom_queue import CustomQueuedata
from ..domain.custom_data_frame import CustomDataframe
class AiVisionController:
    # detection object
    def detectionObjectsFromFrame(frame):
        x, y, w, h = yolo.detection_object(frame)
        center_x = (x + w )// 2
        center_y = (y + h) // 2
        return x,y,w,h,center_x,center_y
    # function to detection and draw the rectangle

    def detectionObjectsAndDrowRectangleFromFrame(frame:CustomDataframe):
        _,_,_,_,center_x,center_y = AiVisionController.detectionObjectsFromFrame(frame)
        AiVisionController.drawRectangle(frame,center_x,center_y)

    # draw rectangle
    def drawRectangle(frame:CustomDataframe):
        cv2.rectangle(frame.frame, (frame.center_x, frame.center_y), (frame.center_x, frame.center_y), (0, 0, 255), 3)
        return frame.frame


    def handelQueueFrames(queue:CustomQueuedata):
        x=[]
        y=[]
        i:CustomDataframe
        for  i in queue.listdataqueue:
        
            x.append(i.center_x)
            y.append(i.center_y)
        fig = plt.figure()
        ax = fig.add_subplot(111)


        ax.scatter(x, y, c='r', marker='o')
        ax.plot(x, y, c='b')

        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        slopes_x=x
        slopes_y=y
        directions = []

        for i in range(len(slopes_x)-1):


           if maths.fabs(320-slopes_x[i])<=20:
                directions.append("f")
           else:
            if maths.fabs(slopes_x[i] - slopes_x[i+1])>5:
                if 320-slopes_x[i]<=0:
                     directions.append("Right")
                else:
                    directions.append("Left")


        for i in range(len(directions)):
            if directions[i] == "Right":
                print(f"Between points {i} and {i + 1}: Right")
            elif directions[i] == "f":
                print(f"Between points {i} and {i + 1}: f")

            elif directions[i] == "Left" and i > 0:
                print(f"Between points {i} and {i + 1}: Left")



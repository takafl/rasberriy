import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import  yolo
import  math as maths
import AiVisionController as aic
class CustomDataframe():
         def __init__(self, arry=np.array,center_x=0,center_y=0):
            self.frame = arry
            self.center_x=center_x
            self.center_y=center_y
            self.rectangle_drawn = False

         # def draw_bounding_boxes(self):

         #         x, y, w, h = yolo.detection_object(self.frame)
         #         self.center_x = (x + w )// 2
         #         self.center_y = (y + h) // 2
         #         cv2.rectangle(self.frame, (self.center_x, self.center_y), (self.center_x, self.center_y), (0, 0, 255), 3)
         #         return self.frame

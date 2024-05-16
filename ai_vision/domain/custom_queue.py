import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import  yolo
import  math as maths
from typing import List

from custom_data_frame import   CustomDataframe  

class CustomQueuedata():
    def __init__(self,):
        self.listdataqueue=List[CustomDataframe]
    def appent2list(self,a:CustomDataframe):
            if len(self.listdataqueue)<10:
             self.listdataqueue.append(a)
            else:
                self.listdataqueue.pop(0)
                self.listdataqueue.append(a)
    # def calcluat(self,x,y):
    #     dist=maths.sqrt(maths.fabs(x-320)**2+maths.fabs(y-240)**2)
    #     tetha=maths.cos(maths.fabs(x-320)/69.4)
    #     tetha=maths.degrees(tetha)
    # def draw3d(self):
    #     x=[]
    #     y=[]

    #     for  i in self.listdataqueue:
    #         i=i 
    #         x.append(i.center_x)
    #         y.append(i.center_y)
    #         self.calcluat(i.center_x, i.center_y)
    #     fig = plt.figure()
    #     ax = fig.add_subplot(111)


    #     ax.scatter(x, y, c='r', marker='o')
    #     ax.plot(x, y, c='b')

    #     ax.set_xlabel('X Axis')
    #     ax.set_ylabel('Y Axis')
    #     slopes_x=x
    #     slopes_y=y
    #     directions = []

    #     for i in range(len(slopes_x)-1):


    #        if maths.fabs(320-slopes_x[i])<=20:
    #             directions.append("f")
    #        else:
    #         if maths.fabs(slopes_x[i] - slopes_x[i+1])>5:
    #             if 320-slopes_x[i]<=0:
    #                  directions.append("Right")
    #             else:
    #                 directions.append("Left")


    #     for i in range(len(directions)):
    #         if directions[i] == "Right":
    #             print(f"Between points {i} and {i + 1}: Right")
    #         elif directions[i] == "f":
    #             print(f"Between points {i} and {i + 1}: f")

    #         elif directions[i] == "Left" and i > 0:
    #             print(f"Between points {i} and {i + 1}: Left")

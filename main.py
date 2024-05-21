import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import  yolo
import  math as maths
class queuedata():
    def __init__(self):
        self.listdataqueue=[]
    def appent2list(self,a):
            if len(self.listdataqueue)<10:
             self.listdataqueue.append(a)
            else:
                self.listdataqueue.pop(0)
                self.listdataqueue.append(a)
    def calcluat(self,x,y):


        dist=maths.sqrt(maths.fabs(x-320)**2+maths.fabs(y-240)**2)
        tetha=maths.cos(maths.fabs(x-320)/69.4)
        tetha=maths.degrees(tetha)
    def draw3d(self):
        x=[]
        y=[]
        for i in self.listdataqueue:
            x.append(i.center_x)
            y.append(i.center_y)
            self.calcluat(i.center_x, i.center_y)
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



class Dataframe():
         def __init__(self, arry=np.array):
            self.frame = arry

            self.rectangle_drawn = False

         def draw_bounding_boxes(self):

                 x, y, w, h = yolo.detection_object(self.frame)
                 self.center_x = (x + w )// 2
                 self.center_y = (y + h) // 2
                 cv2.rectangle(self.frame, (self.center_x, self.center_y), (self.center_x, self.center_y), (0, 0, 255), 3)
                 return self.frame




cap = cv2.VideoCapture(0)
i=0
q=queuedata()
while i<20:
    ret, frame = cap.read()


    if not ret:
        break  # Break the loop if the video is over
    h,w,_=frame.shape
    cv2.rectangle(frame, (w//2, h//2), (w//2, h//2), (0, 0, 255), 3)

    aa = Dataframe(frame)
    frame1 = aa.draw_bounding_boxes()
    cv2.imshow("test", frame1)
    q.appent2list(aa)
    # time.sleep(1)
    i=i+1
    if i==9:
        q.draw3d()
        i=0
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




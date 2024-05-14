import sys
sys.path.append('/home/anas/site-packages')

import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
# import testmodel
import  yolo
class queuedata():
    def __init__(self):
        self.listdataqueue=[]
    def appent2list(self,a):
            if len(self.listdataqueue)<10:
             self.listdataqueue.append(a)
            else:
                self.listdataqueue.pop(0)
                self.listdataqueue.append(a)


    def draw3d(self):
        x=[]
        y=[]

        for i in self.listdataqueue:
            x.append(i.center_x)
            y.append(i.center_y)



            # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Plot the points in 3D space
        ax.scatter(x, y, c='r', marker='o')
        ax.plot(x, y, c='b')
        # Set labels for the axes
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')


        # Display the plot
        # plt.show()

        slopes_x=x
        slopes_y=y
        # Determine the direction based on changes in coordinates
        directions = []
        print(slopes_x[0])
        print(slopes_x)

        for i in range(len(slopes_x)-1):



            if slopes_x[i] - slopes_x[i+1]>5:

                directions.append("Right")
            elif slopes_x[i] - slopes_x[i+1]<-5:
                directions.append("Left")
            # else:
            #     directions.append("No horizontal movement")
            #
            # if slopes_y[i] > slopes_y[i+1]:
            #     directions.append("Up")
            # elif slopes_y[i] < slopes_y[i+1]:
            #     directions.append("Down")
            # else:
            #     directions.append("No vertical movement")

        # Print movement directions
        for i in range(len(directions)):
            if directions[i] == "Right":
                print(f"Between points {i} and {i + 1}: Right")
            elif directions[i] == "Up":
                print(f"Between points {i} and {i + 1}: Up")
            elif directions[i] == "Left" and i > 0:
                print(f"Between points {i} and {i + 1}: Left")
            elif directions[i] == "Down" and i > 0:
                print(f"Between points {i} and {i + 1}: Down")


class Dataframe():
         def __init__(self, arry=np.array):
            self.frame = arry

            self.rectangle_drawn = False

         def draw_bounding_boxes(self):

                 x, y, w, h = yolo.detection_object(self.frame)
                 self.center_x = x + w // 2
                 self.center_y = y + h // 2
                 return self.frame




cap = cv2.VideoCapture(0)
i=0
q=queuedata()
while i<20:
    ret, frame = cap.read()


    if not ret:
        break  # Break the loop if the video is over

    # image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # gray_frame = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)



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




import doctest
import cv2
import os
import numpy as np

min_rad=10
max_rad=100
param1=50
param2=30

if not os.path.exits('output'):
  os.makedirs('output')

  def find_color_diff(image, circle_center, circle_radius, ref_color):
    x,y=cicle_center
    radius=circle_radius
    circle_region=image[y-radius:y+radius, x-radius:x+radius]

    color_diff=np.sum(np.abs(circle_region-ref_color))

    return color_diff
   
    circle_colors=[(0,255,255),(0,0,255)]


  for image_file in os.listdir('imgs'):
    img=cv2.imread(f"imgs/{car.}", cv2.IMREAD_COLOR)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    circles=cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=38 , maxRadius=80)
    if circles is not None:
      circles=circles[0,:] astype(int)
      for i, circle inenumerate(circles):
        center=(circle[0], circle[1])
        radius=circle[2]


        ref_color=img[circle[1],circle[0]]

        color_diff=find_color_diff(img,center,radius,ref_color)

        if color_diff>1:
          circle_region=img[circle[1]-radius:circle[1]+ radius, circle[0]-radius:circle[0]+radius]

          seg_circle=seg_img(circle_region)
          unique_col=np.unique(seg_circle.reshape(-1,3),axis=0)
          num_unique_img=len(unique_col)
          if num_unique_img>1:
            color=circle_colors[i%len(circles_colors)]

        else:
            color=(0,0,255)
            cv2.circle(img,center,radius,color,2)
        else:
            cv2.circle(img,center,radius,(0,255,0),2)



            cv2.imwrite('result.png', img)
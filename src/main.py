import cv2
from cv2 import aruco
import numpy as np
import os
import matplotlib.pyplot as plt

def transform_to_top_view():
    p_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    img = cv2.imread('sample_img/inu.jpg') # Load image
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, p_dict) # detect markers
    
    # set marker center location
    m = np.empty((4,2))
    corners2 = [np.empty((1,4,2))]*4
    for i,c in zip(ids.ravel(), corners):
        corners2[i] = c.copy()
    m[0] = corners2[0][0][2]
    m[1] = corners2[1][0][3]
    m[2] = corners2[2][0][0]
    m[3] = corners2[3][0][1]

    width, height = (500,500) # set top view image size
    
    marker_coordinates = np.float32(m)
    true_coordinates   = np.float32([[0,0],[width,0],[width,height],[0,height]])
    trans_mat = cv2.getPerspectiveTransform(marker_coordinates,true_coordinates) # get transformation matrix
    img_trans = cv2.warpPerspective(img,trans_mat,(width, height))
    plt.imshow(img_trans)
    plt.show()
    
def detect_marker_zero():
    p_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    img = cv2.imread('sample_img/m0-photo.jpg')  
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, p_dict) # 検出
    img_marked = aruco.drawDetectedMarkers(img.copy(), corners, ids)   # 検出結果をオーバーレイ
    plt.imshow(img_marked)
    plt.show()
    
if __name__ == "__main__":
    transform_to_top_view()
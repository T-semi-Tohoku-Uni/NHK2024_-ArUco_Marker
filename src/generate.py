from cv2 import aruco
import cv2
import os

def generate_aruco_dict():
    """
    すでに生成済みのマーカーを生成する
    マーカーの対応は以下の通り
    0: 左上
    1: 右上
    2: 右下
    3: 左下
    4: ロボットに取り付ける
    
    Markerディレクトリ以下にマーカーが生成される
    """
    p_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    marker = [0] * 5 # Initialize marker
    dir = 'Marker'
    for i in range(len(marker)):
        marker[i] = aruco.generateImageMarker(p_dict, i, 75)
        filename = os.path.join(dir, f'Marker{i}.png')
        cv2.imwrite(filename, marker[i])

if __name__ == "__main__":
    generate_aruco_dict()
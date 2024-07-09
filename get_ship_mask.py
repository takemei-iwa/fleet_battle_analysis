import os

import cv2
import numpy as np
import json
import argparse

ship_mask_dir = "ship_mask"
def get_ship_mask(img_path):
    # 画像を読み込む
    img = cv2.imread(img_path)

    height, width, _ = img.shape

    #白1
    LOW_COLOR1 = np.array([0, 0, 250]) # 各最小値を指定
    HIGH_COLOR1 = np.array([10, 10, 255]) # 各最大値を指定

    #白2
    LOW_COLOR2 = np.array([230, 230, 250]) # 各最小値を指定
    HIGH_COLOR2 = np.array([255, 255, 255]) # 各最大値を指定

    #白3
    LOW_COLOR3 = np.array([230, 0, 250]) # 各最小値を指定
    HIGH_COLOR3 = np.array([255, 10, 255]) # 各最大値を指定

    #白2
    LOW_COLOR4 = np.array([0, 230, 250]) # 各最小値を指定
    HIGH_COLOR4 = np.array([10, 255, 255]) # 各最大値を指定

    #背景
    lower_back = np.array([150, 50, 50]) # 各最小値を指定
    upper_back = np.array([170, 200, 230]) # 各最大値を指定

    lower_white = np.array([0, 0, 250])
    upper_white = np.array([255, 255, 255])


    # マスクを作成
    


    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
    backmask = cv2.inRange(hsv, lower_back, upper_back)
    whitemask1 = cv2.inRange(hsv, LOW_COLOR1, HIGH_COLOR1)
    whitemask2 = cv2.inRange(hsv, LOW_COLOR2, HIGH_COLOR2)
    whitemask3 = cv2.inRange(hsv, LOW_COLOR1, HIGH_COLOR3)
    whitemask4 = cv2.inRange(hsv, LOW_COLOR1, HIGH_COLOR4)
    whitemask = whitemask1 + whitemask2 + whitemask3 + whitemask4


    test = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    backmask = 255 - backmask
    
    mask = backmask
    output_path = \
        os.path.join(ship_mask_dir,os.path.basename(img_path))
    cv2.imwrite(output_path, mask)  
    
def get_ship_point(img_path):
    input_path = \
        os.path.join(ship_mask_dir,os.path.basename(img_path))
    img = cv2.imread(input_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width, _ = img.shape

    points=[]

    
    
    sum = 0
    for x in range(0,10):
        for y in range(0,10):
            sum=0
            for i in range(10):
                for j in range(10):
                    if img_gray[int(y*(height / 10)+j+(height/10/4))][int(x*(height / 10)+i+(height/10/4))] > 200 :
                        sum+=1
            if sum > 10:
                points.append({"x": int(x), "y": int(y)})        
    output_path = \
        os.path.join("ship_point",os.path.basename(img_path)[:-4]+".json")
    #print(points)
    with open(output_path, 'w',encoding='utf-8') as json_file:
        json.dump(points, json_file, indent=4,ensure_ascii=False)


def get_white_mark_point(img_path, template_path):
    img = cv2.imread(img_path)
    template = cv2.imread(template_path)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
  
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    w, h = template_gray.shape[::-1]

    threshold = 0.5
    loc = np.where( result >= threshold)
    # マッチした領域の座標を取得し、リストに格納
    points = []
    height,_,_ = img.shape
    for pt in zip(*loc[::-1]):
        cont = False
        
        x = int((pt[0]+w) / (height / 10))
        y = int((pt[1]+h) / (height / 10))
        for point in points:
            if point['x'] == x and point['y'] == y:
                cont = True
        if cont:
            continue
        points.append({"x": x, "y": y})
    # JSON形式でファイルに保存
    output_path = \
        os.path.join("white_mark_point",os.path.basename(img_path)[:-4]+".json")
    with open(output_path, 'w') as json_file:
        json.dump(points, json_file, indent=4)
    
import json
import cv2
import numpy as np

whole_data_path = "whole_data.json"

def sum_data(games):
    sum = [[0 for i in range(10)] for j in range (10)]
    for points in games:
        for point in points:
            sum[point[0]][point[1]]+=1
    return sum

  
def draw_grid_with_rectangles(height, width, data):
    grid_size = 10

    img = np.ones((height, width,3), dtype=np.uint8) * 255

    # マス目のサイズを計算
    cell_height = height // grid_size
    cell_width = width // grid_size

    # 画像にマス目を描画
    for i in range(1, grid_size):
        # 垂直線を描画
        cv2.line(img, (i * cell_width, 0), (i * cell_width, height), (0, 0, 0), 1)
        # 水平線を描画
        cv2.line(img, (0, i * cell_height), (width, i * cell_height), (0, 0, 0), 1)

    # 長方形を描画
    max=np.max(data)
    min=np.min(data)

    for x in range(10):
        for y in range(10):
            count = data[x][y]
            possi = (count - min) / (max - min) * 100
            print(f"{count}, {possi}")
            if possi >= 75 :
                r = 250
                g = int(250 - (possi - 75)/25 * 250)
                b = 0
            elif possi >= 50:
                g = 250
                r = int((possi - 50)/25 * 250)
                b = 0
            elif possi >= 25:
                g = 250
                b = int(250 - (possi - 25)/25 * 250)
                r = 0
            else :
                b = 250
                g = int(possi/25 * 250)
                r = 0
            top_left = (x * cell_width+1, y * cell_height+1)
            bottom_right = ((x + 1) * cell_width-1, (y + 1) * cell_height-1)
            hsv_image_with_shape = cv2.rectangle(img, top_left, bottom_right, (b,g,r), -1)
    return img

with open(whole_data_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
points = sum_data(data)
print(points)
canvas = draw_grid_with_rectangles(500,500,points)
cv2.imwrite("sum_data_canvas.jpg",canvas)



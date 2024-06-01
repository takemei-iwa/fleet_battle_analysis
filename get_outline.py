import cv2
import numpy as np

# 画像を読み込む
image_path = '001.jpg'
img = cv2.imread(image_path)

height, width, _ = img.shape
print(f"shape : {height}, {width}")
img = img[0:int(height/2)]

'''
LOW_COLOR1 = np.array([32, 84, 214]) # 各最小値を指定
#LOW_COLOR1 = np.array([0, 0, 0]) # 各最小値を指定
HIGH_COLOR1 = np.array([42, 122, 250]) # 各最大値を指定
'''
LOW_COLOR1 = np.array([32, 50, 190]) # 各最小値を指定
HIGH_COLOR1 = np.array([42, 180, 250]) # 各最大値を指定

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
mask = cv2.inRange(hsv, LOW_COLOR1, HIGH_COLOR1) # マスクを作成

cv2.imwrite("mask.jpg", mask)

# マスク画像から輪郭を検出
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 各輪郭を囲む長方形領域を抽出
extracted_regions = []
for contour in contours:
    print("hey")
    if cv2.contourArea(contour) > 100:  # ノイズを除去するために面積の閾値を設定
        x, y, w, h = cv2.boundingRect(contour)
        if (w*h) / (height*width) < 0.1:
            continue
        print((w*h) / (height*width))
        extracted_region = img[y:y+h, x:x+w]
        extracted_regions.append(extracted_region)
        # 抽出した領域をデバッグ用に表示するために長方形を描画
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 抽出した領域を保存または表示
for i, region in enumerate(extracted_regions):
    output_region_path = f'extracted_region_{i}.jpg'
    cv2.imwrite(output_region_path, region)

# 結果の画像を保存
output_image_path = 'detected_regions.jpg'
cv2.imwrite(output_image_path, img)

print(f"shape : {height}, {width}")
'''
# 画像を表示
cv2.imshow("Detected Regions", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''

contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255, 0, 0), 3, cv2.LINE_AA)
cv2.imwrite("out_img.jpg",  img) # 書き出す
cv2.imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()


masked_img = cv2.bitwise_and(img, img, mask= mask) # 元画像から特定の色を抽出
cv2.imwrite("out_img.jpg", mask) # 書き出す
cv2.imshow("Detected Ships", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
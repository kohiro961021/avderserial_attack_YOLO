import os
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

model = YOLO(r"D:\Code\anaconda\code\adverserial_attack\runs\detect\train\weights\best.pt")
# 設定圖片資料夾
image_dir = r"D:\Code\anaconda\code\adverserial_attack\新增資料夾"

# 讀取所有圖片
all_images = os.listdir(image_dir)
selected_images = all_images[:45]


# 逐一處理圖片
for img_name in selected_images:
    img_path = os.path.join(image_dir, img_name)

    # 預測圖片
    results = model.predict(img_path)

    # 讀取圖片
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV 讀取的是 BGR 格式，轉換為 RGB

    # 如果 YOLO 有偵測到物件，顯示偵測結果
    if results[0].boxes and len(results[0].boxes) > 0:
        plotted_img = results[0].plot()  # results[0] 是第一張圖片的結果
        print(f"Detections found in {img_name}.")
    else:
        plotted_img = img  # 如果沒有偵測到物件，顯示原圖
        print(f"No detections for {img_name}, showing original image.")

    # 顯示結果圖片
    plt.figure(figsize=(8, 6))
    plt.imshow(plotted_img)
    plt.axis('on')  # 關閉座標軸顯示
    plt.show()

# 🛑 Adversarial Attack on YOLOv8 & YOLOv10

本專案專注於 **對抗性攻擊 (Adversarial Attacks)** 在物件偵測模型 YOLOv8 與 YOLOv10 上的實作與分析，  
特別針對智慧駕駛中的交通標誌辨識系統，探討白箱與黑箱攻擊下模型的脆弱性。  

> 🎯 科展題目：「看的見卻認不出來 —— Adversarial Attack 對於辨識路標的危害」

---

## 📂 專案結構

adverserial_attack/
│
├── adv_images/ # FGSM / PGD 攻擊結果
├── adv_single_image/ # 單張圖片攻擊測試
├── outcmaes/ # CMA-ES 黑箱攻擊輸出
├── result/ / results/ # 攻擊結果可視化 (信心值、類別變化)
├── runs/ # YOLO 推論輸出 (Ultralytics 預設)
├── YOLOv10/ # YOLOv10 相關程式碼
│
├── attack.ipynb # 白箱攻擊流程 (FGSM / PGD)
├── blackbox.ipynb # 黑箱攻擊流程 (CMA-ES / Boundary)
├── basic_model(yolov8).ipynb # YOLOv8 基準推論測試
├── YOLOv8.py # YOLOv8 推論腳本
│
├── yolov8n.pt / yolov8s.pt # YOLOv8 預訓練權重
├── *.png # 攻擊結果圖表 (patch / diff / score)
└── README.md

yaml
複製程式碼

---

## 🧪 攻擊方法

### 🔹 白箱攻擊 (White-box)
- **FGSM (Fast Gradient Sign Method)**  
- **PGD (Projected Gradient Descent)**  

👉 基於梯度的快速攻擊，能精準生成對抗樣本。
但是這個是基於transfer attack
---

### 🔹 黑箱攻擊 (Black-box)
- **CMA-ES (Covariance Matrix Adaptation Evolution Strategy)**  
- **Boundary Attack**  

👉 不需模型權重，只依賴模型輸出結果進行優化，能應用於閉源系統。

---

## 輸出結果
對抗樣本圖片 → adv_images/

信心值變化圖表 → results/

最佳擾動 patch → outcmaes/

📊 攻擊效果展示
🎯 原圖 vs 對抗圖
原始輸入	對抗樣本

📌 結論
FGSM / PGD：快速且有效，但需白箱存取權限。

CMA-ES / Boundary：即使未知模型內部，也能顯著降低 YOLO 的信心值。

智慧駕駛風險：對抗樣本可能誤導交通標誌辨識，造成潛在安全問題。

📝 License
本專案僅用於 研究與教育用途。
⚠️ 請勿將此技術用於任何惡意行為。

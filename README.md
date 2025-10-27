# 🔢 Digit-2 Detector using Logistic Regression & Streamlit

A **machine learning web app** built with **Logistic Regression** and the **MNIST dataset** that detects whether a hand-drawn digit is the number **2**.

---

## 🚀 Features

- 🖊️ Draw any digit on a **canvas** and let the model predict it  
- 🧮 Uses a **trained Logistic Regression model** trained on **MNIST**  
- 🎨 Real-time drawing interface powered by **Streamlit Drawable Canvas**  
- 💾 Model loading handled via **joblib**  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Canvas Drawing | streamlit-drawable-canvas |
| Machine Learning | scikit-learn (Logistic Regression) |
| Model Storage | joblib |
| Dataset | MNIST Handwritten Digits |

---

## 🧠 How It Works

1. User **draws a digit** on the interactive canvas  
2. The drawing is **converted to grayscale**, **resized to 28×28**, and **flattened**  
3. The Logistic Regression model predicts if the digit is a **2** or not  
4. Streamlit displays the **predicted digit** interactively  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/digit-2-detector.git
   cd digit-2-detector

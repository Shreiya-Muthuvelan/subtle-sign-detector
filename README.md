# 🧠 Subtle Sign Detector

A machine learning-powered Streamlit web app that detects early signs of **employee burnout** based on subtle workplace behavior. It uses a **regression-classification pipeline** to predict the **burn rate** and categorize the **burnout risk level** as Low, Moderate, or High — along with wellness suggestions based on the prediction.

---

## 🚀 Demo

🔗 Try the app here: [https://subtle-sign-detector-ka9g5apjnjvkmvufuy8jow.streamlit.app/]

---

## 📌 Features

- 🔥 **Predicts Burn Rate** using a Random Forest Regressor
- 🧯 **Classifies Burnout Risk** (Low / Moderate / High)
- 🌿 **Mental Wellness Suggestions** tailored to the risk level
- 🖥️ User-friendly interface built using **Streamlit**
- 🎨 Aesthetic, dark-mode themed UI aligned with mental health tone

---

## 🧠 ML Workflow

1. **Data Cleaning & Preprocessing**  
   - Handled missing values  
   - Selected key features based on correlation and interpretability

2. **Modeling**  
   - Regression Model: Random Forest Regressor to predict burn rate  
   - Classification Model: Random Forest Classifier to predict burnout level based on burn rate  

3. **Deployment**  
   - Streamlit for frontend  
   - Hosted on Streamlit Community Cloud  

---

## 📥 Input Parameters

| Feature               | Description                            |
|-----------------------|----------------------------------------|
| Mental Fatigue Score  | Level of mental exhaustion (0 to 10)   |
| Resource Allocation   | Resource load at work (1 to 10)        |
| Days Since Joining    | How long the employee has been working |

---

## 📤 Output

- `Predicted Burn Rate`: A float between 0.0 and 1.0  
- `Burnout Risk Level`: Categorized as **Low**, **Moderate**, or **High**  
- 💡 Personalized **wellness suggestions** based on burnout level

---

# 🧠 Subtle Sign Detector — Machine Learning Web App for Burnout Risk Analysis

A **machine learning-powered Streamlit application** that detects early signs of **employee burnout** from subtle workplace behavior. 

The system predicts the **burn rate** using a Random Forest Regressor and categorizes burnout risk as **Low, Moderate, or High**, offering tailored wellness suggestions for proactive self-care.

---

## 🚀 Live Demo
[![Streamlit App](https://img.shields.io/badge/Try%20the%20App-Streamlit-blue?logo=streamlit)](https://subtle-sign-detector-ka9g5apjnjvkmvufuy8jow.streamlit.app/)

---

## 📌 Key Features
- 🔍 **Burn Rate Prediction** using a trained Random Forest Regressor  
- 🛡 **Risk Classification**: Low / Moderate / High  
- 💡 **Personalized Wellness Suggestions** based on predicted risk  
- 🎨 **Dark Mode UI** designed for a calming, mental-health-friendly experience  
- 🌐 **Deployed on Streamlit Community Cloud** — accessible anywhere

---

## 🧠 Problem & Solution
Burnout is a growing challenge in modern workplaces, often going unnoticed until it impacts productivity and well-being.  

This project provides an **accessible, data-driven tool** to assess burnout risk early, enabling both individuals and HR teams to take timely preventive measures.

---

## ⚙️ ML Workflow
1. **Data Preprocessing**  
   - Imputed missing values using mean/median strategies  
   - Selected features via correlation analysis and interpretability considerations  

2. **Model Development**  
   - Algorithm: Random Forest Regressor for continuous burn rate prediction  
   - Evaluation: R² score and Mean Absolute Error (MAE) for performance assessment  

3. **Deployment**  
   - Frontend: Streamlit for rapid UI development  
   - Hosting: Streamlit Community Cloud with model serialized via Joblib

---

## 📥 Input Parameters

| Feature               | Description                               |
|-----------------------|-------------------------------------------|
| Mental Fatigue Score  | Level of mental exhaustion (0–10)         |
| Resource Allocation   | Resource load at work (1–10)              |
| Designation           | Employee's role or seniority level        |
| WFH Setup Available   | 1 if WFH is available, 0 otherwise        |

---

## 📤 Output

| Output Metric         | Description                                |
|-----------------------|--------------------------------------------|
| Predicted Burn Rate   | Value between 0.0 and 1.0                  |
| Burnout Risk Level    | Low, Moderate, or High category            |
| Wellness Suggestions  | Custom advice based on burnout level       |

---

## 🛠️ Tech Stack

**Languages & Libraries**  
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)  
scikit-learn • Pandas • NumPy • Matplotlib • Seaborn  

**Deployment**  
Streamlit • Joblib • Google Colab

---

## 👩‍💻 Author
**Shreiya Muthuvelan**  
2nd Year CSE @ BITS Pilani Dubai 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/shreiyamuthuvelan/)  

---

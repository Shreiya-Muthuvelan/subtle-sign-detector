# Subtle Sign Detector — Web App for Burnout Risk Analysis

## Project Objective

Employee burnout is a critical and often overlooked challenge affecting workplace productivity and wellbeing. This project presents a **machine learning-powered web application** that detects early signs of burnout from subtle workplace behavior indicators. Powered by a Random Forest Regressor, the system predicts the **burn rate** and categorizes burnout risk into **Low, Moderate, or High**, providing personalized wellness suggestions to support proactive self-care.

---

## Key Features

- Burn rate prediction using a trained Random Forest Regressor  
- Risk classification into Low, Moderate, and High categories  
- Personalized wellness recommendations based on risk level  
- Dark mode user interface focused on mental health usability  
- Deployment on Streamlit Community Cloud for easy accessibility  

---

## Problem and Solution

Burnout often develops gradually and is difficult to detect before it impacts employees’ performance and well-being. This application offers a **data-driven, accessible tool** enabling individuals and HR teams to assess burnout risk early and intervene preventively, helping preserve workforce health and productivity.

---

## Machine Learning Workflow

1. **Data Preprocessing**  
   - Missing values imputed using mean and median strategies  
   - Feature selection based on correlation analysis and interpretability  
2. **Model Development**  
   - Random Forest Regressor trained for continuous burn rate prediction  
   - Model evaluated using R² score and Mean Absolute Error (MAE)  
3. **Deployment**  
   - User interface developed using Streamlit for rapid prototyping  
   - Model serialization via Joblib and hosted on Streamlit Community Cloud  

---

## Input Parameters

| Feature              | Description                             |
|----------------------|---------------------------------------|
| Mental Fatigue Score  | Level of mental exhaustion (0–10)     |
| Resource Allocation   | Workload/resource load (1–10)          |
| Designation          | Employee’s role or seniority level     |
| WFH Setup Available  | 1 if work-from-home setup is available, 0 otherwise |

---

## Output

| Output Metric        | Description                           |
|---------------------|-------------------------------------|
| Predicted Burn Rate  | Continuous value between 0.0 and 1.0 |
| Burnout Risk Level   | Categorized as Low, Moderate, or High |
| Wellness Suggestions | Tailored advice based on risk level  |

---
## App Preview
<img src="app_inputs.jpg" width="600" >


<img src="app_ouputs.jpg" width="600">

---

## Tech Stack

**Languages & Libraries:**  
Python 3.10, scikit-learn, Pandas, NumPy, Matplotlib, Seaborn  

**Deployment:**  
Streamlit, Joblib, Google Colab  

---

## Usage


A live demo of the app is available here:  
[Try the App on Streamlit](https://subtle-sign-detector-ka9g5apjnjvkmvufuy8jow.streamlit.app/)


---

##  Author
**Shreiya Muthuvelan**  
3rd Year CSE @ BITS Pilani Dubai 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/shreiyamuthuvelan/)  

---

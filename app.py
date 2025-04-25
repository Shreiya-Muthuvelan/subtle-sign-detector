import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Subtle Sign Detector", page_icon="🧠")

regressor = joblib.load('burnout_regressor.pkl')
def categorize_risk(burn_rate):
    if burn_rate < 0.3:
        return "Low"
    elif burn_rate < 0.7:
        return "Moderate"
    else:
        return "High"


st.title("🧠 Subtle Sign Detector")
st.subheader("Detect burnout levels and receive mental wellness suggestions")

st.markdown("---")


st.markdown("#### 📥 Input Details")
mental_fatigue = st.slider("🧠 Mental Fatigue Score", 0.0, 10.0, 5.0)
resource_alloc = st.slider("⚙️ Resource Allocation (1-10)", 1, 10, 5)
designation=st.slider("🖥️ Designation(0-5)",0,5,2)
is_available = st.checkbox("🏠 Is WFH Setup Available?")
is_available_encoded = int(is_available)  # True → 1, False → 0

st.markdown("---")

# Predict Button
if st.button("🔍 Predict Burnout"):
    input_data = np.array([[mental_fatigue,resource_alloc,  designation,is_available_encoded]])
    burn_rate = regressor.predict(input_data)[0]
    
    risk_label_numeric = categorize_risk(burn_rate)
    st.markdown(f"### 🔥 Predicted Burn Rate: `{burn_rate:.2f}`")
    st.markdown(f"### 😫 Burnout Risk Level: `{risk_label_numeric}`")
    st.markdown("---")

    st.markdown("### 💡 Mental Wellness Suggestions:")

    if risk_label_numeric == "Low":
        st.success("""
        - ✅ Keep up your healthy routine  
        - 🌿 Take short breaks during the day  
        - 📖 Try reading or relaxing hobbies  
        - 😌 Maintain work-life balance
        """)

    elif risk_label_numeric == "Moderate":
        st.warning("""
        - 🧘 Practice mindfulness or short meditations  
        - 💤 Improve sleep hygiene and hydration  
        - 🚶‍♀️ Include light exercise in daily routine  
        - 🗓️ Reassess workload and time management
        """)

    elif risk_label_numeric == "High":
        st.error("""
        - 🛑 Consider taking a mental health day  
        - 🗣️ Talk to a friend, mentor, or counselor  
        - 🧑‍⚕️ Seek professional support if needed  
        - 🧩 Try grounding exercises like journaling  
        - ⛔ Set clear work boundaries
        """)

    st.markdown("---")
    st.markdown("💙 *Take care of your mind, it's the strongest asset you have.*")

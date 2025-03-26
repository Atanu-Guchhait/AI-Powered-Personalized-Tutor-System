import streamlit as st
import pandas as pd
import time
import pickle  

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="📊 Student Assessment Score Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---- LOAD MODEL ----
with open("Assesment score.pkl", "rb") as model_file:  # Change model filename if needed
    pipeline = pickle.load(model_file)

# ---- CUSTOM CSS FOR WHITE THEME ----
st.markdown("""
    <style>
        /* Background and general styling */
        .main {
            background-color: #ffffff;  /* White background */
            color: #000000;  /* Black text */
        }
        
        /* Header */
        h1, h2, h3, p {
            text-align: center;
            color: #000000;  /* Black header text */
        }
        
        /* Form Styling */
        .stNumberInput, .stSelectbox, .stTextInput, .stSlider {
            background-color: #ffffff;  /* White background */
            color: #000000;  /* Black text */
            border-radius: 8px;
            padding: 10px;
            transition: 0.3s;
        }
        
        /* Button Styling */
        div.stButton > button {
            background-color: #4CAF50;  /* Green button */
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 12px 30px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #388E3C;  /* Darker green on hover */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }

        /* Cards */
        .card {
            background: #f9f9f9;  /* Light gray background */
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
            transition: 0.3s;
            margin: 15px;
            text-align: center;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
        }
        
        /* Results */
        .success {
            color: #4CAF50;  /* Green success text */
        }
        .error {
            color: #E53935;  /* Red error text */
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #000000;  /* Black footer text */
        }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<h1>📊 Student Assessment Score Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p>Fill in the details below to predict the student's assessment score.</p>", unsafe_allow_html=True)

# ---- FORM ----
with st.form("assessment_form"):
    # Two-column layout
    col1, col2 = st.columns(2)

    # 🛠️ Column 1
    with col1:
        age = st.number_input("📅 Age", min_value=4, max_value=18, value=6)
        gender = st.selectbox("👦 Gender", ['Male', 'Female'])
        parental_education = st.selectbox("🎓 Parental Education Level", ['High School', 'College', 'Postgraduate'])
        earning_class = st.selectbox("💰 Earning Class", ['Low', 'Medium', 'High'])
        level = st.selectbox("🏫 Student Level", ['Kindergarten', 'Elementary', 'Middle School', 'High School'])

    # 🛠️ Column 2
    with col2:
        course_level = st.selectbox("📘 Course Level", ['Low', 'Medium', 'High'])
        material_level = st.selectbox("📖 Material Level", ['Low', 'Medium', 'High'])
        previous_scores = st.number_input("📊 Previous Scores (out of 100)", min_value=0, max_value=100, value=89)
        iq = st.number_input("🧠 IQ", min_value=50.0, max_value=140.0, value=100.0)
        attendance = st.number_input("📅 Attendance (out of 100)", min_value=0, max_value=100, value=86)

    # Study Time Slider
    study_time = st.slider("⏳ Study Time (hours per Day)", min_value=0.0, max_value=20.0, value=4.10, step=0.1)

    # Submit Button
    submitted = st.form_submit_button("🔍 Predict")

# ---- PREDICTION ----
if submitted:
    # Preparing input data
    input_data = pd.DataFrame([[  
        age, gender, parental_education, earning_class, level,  
        course_level, material_level, previous_scores, iq, attendance, study_time  
    ]], columns=[  
        "Age", "Gender", "Parental_Education_Level", "Earning Class", "Level",  
        "Course Level", "Material Level", "Previous_Scores", "IQ", "Attendance", "Study Time"  
    ])

    # Smooth loading animation
    with st.spinner("🔄 Running prediction..."):
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)

    # Making the prediction
    predicted_score = pipeline.predict(input_data)[0]

    # ---- RESULT DISPLAY ----
    st.markdown("<h2>📊 Prediction Result</h2>", unsafe_allow_html=True)

    # Displaying result in an elegant card
    st.markdown(
        f"""
        <div class="card">
            <h3 class="success">📈 Predicted Assessment Score: {predicted_score:.2f} / 100</h3>
            <p>🎯 Keep up the good work! Consistent performance and dedication lead to success.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Celebration effects
    st.balloons()  


# ---- FOOTER ----
st.markdown('<div class="footer">🎓 Developed by <a href="https://www.linkedin.com/in/atanu-guchhait-4a6427296/" target="_blank">Atanu</a> | © 2025</div>', unsafe_allow_html=True)
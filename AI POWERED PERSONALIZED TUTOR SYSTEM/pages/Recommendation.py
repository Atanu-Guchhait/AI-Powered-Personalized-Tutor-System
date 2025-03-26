import streamlit as st
import pandas as pd
import pickle

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="📚 Learning Material Recommendation",
    page_icon="📘",
    layout="wide"
)

# ---- LOAD ML MODEL ----
with open("recomendation.pkl", "rb") as f:
    pipeline = pickle.load(f)

# ---- RECOMMENDED MATERIALS ----
recommended_material = {
    3: [
        {"name": "📚 Adventure Academy", "link": "https://www.adventureacademy.com/", "description": "A virtual world for learning."},
        {"name": "📖 Scholastic Learn at Home", "link": "https://classroommagazines.scholastic.com/", "description": "Daily learning projects for kids."},
        {"name": "➕ CoolMath4Kids", "link": "https://www.coolmath4kids.com/", "description": "Math games and lessons for kids."}
    ],
    1: [
        {"name": "💻 CK-12 Interactive Learning", "link": "https://www.ck12.org/", "description": "Free STEM resources for students."},
        {"name": "🚀 NASA STEM Engagement", "link": "https://www.nasa.gov/stem/", "description": "Explore space and science with NASA."},
        {"name": "📚 Quizlet Study Sets", "link": "https://quizlet.com/", "description": "Create and study flashcards."}
    ],
    0: [
        {"name": "📚 PBS Kids Learning Games", "link": "https://pbskids.org/", "description": "Interactive games for young learners."},
        {"name": "🎓 Sesame Street Learning", "link": "https://www.sesamestreet.org/", "description": "Fun and educational content for kids."},
        {"name": "🌍 National Geographic Kids", "link": "https://kids.nationalgeographic.com/", "description": "Explore the world with Nat Geo Kids."}
    ],
    2: [
        {"name": "🎓 Harvard Online Courses", "link": "https://online-learning.harvard.edu/", "description": "Free courses from Harvard University."},
        {"name": "📚 Stanford Online", "link": "https://online.stanford.edu/", "description": "Online courses from Stanford."},
        {"name": "🌐 Coursera Courses", "link": "https://www.coursera.org/", "description": "Learn from top universities worldwide."}
    ]
}

# ---- CSS STYLING ----
st.markdown("""
    <style>
    /* Simple and clean white theme */
    .main {
        background-color: #ffffff;  /* White background */
        color: #333333;  /* Dark gray text */
        padding: 20px;
        border-radius: 12px;
    }
    /* Header Styling */
    h1 {
        text-align: center;
        color: #333333;  /* Dark gray text */
        font-size: 3rem;
        margin-bottom: 10px;
    }
    h2 {
        color: #333333;  /* Dark gray text */
        font-size: 2rem;
        margin-bottom: 10px;
    }
    h3 {
        color: #333333;  /* Dark gray text */
        font-size: 1.5rem;
    }
    /* Button Styling */
    .stButton>button {
        background-color: #007bff;  /* Blue button */
        color: #ffffff;  /* White text */
        padding: 12px 25px;
        font-size: 16px;
        border-radius: 8px;
        transition: 0.3s;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #0056b3;  /* Darker blue on hover */
        box-shadow: 0 5px 15px rgba(0, 123, 255, 0.3);
    }
    /* Card Styling */
    .card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
        background-color: #f9f9f9;  /* Light gray background */
        margin: 10px 0;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    /* Link Styling */
    a {
        text-decoration: none;
        color: #007bff;  /* Blue link */
        font-weight: bold;
        border-bottom: 2px solid #007bff;
    }
    a:hover {
        color: #0056b3;  /* Darker blue on hover */
        border-bottom: 2px solid #0056b3;
    }
    /* Footer Styling */
    .footer {
        text-align: center;
        padding: 20px;
        font-size: 14px;
        color: #777777;  /* Gray text */
    }
    /* Ensure input labels are visible */
    .stNumberInput label, .stSelectbox label, .stTextInput label {
        color: #333333 !important;  /* Dark gray text */
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown(
    """
    <h1>📘 Student Learning Material Recommendation</h1>
    <p style='text-align: center; font-size: 18px; color: #555555;'>
        🔹 Predict the student’s learning level and receive personalized learning resources.
    </p>
    """,
    unsafe_allow_html=True
)

# ---- INPUT FORM ON MAIN PAGE ----
with st.container():
    st.markdown("### **📊 Enter Student Details**")
    with st.form("student_details_form"):
        # Create 3 columns for the input sections
        col1, col2, col3 = st.columns(3)

        # Column 1: Student Information
        with col1:
            
            age = st.number_input("🧒 **Age**", min_value=3, max_value=18, value=6, help="Enter the student's age.")
            level = st.selectbox("🏫 **Level**", ["Kindergarten", "Elementary", "Middle School", "High School"], help="Select the student's education level.")
            iq = st.number_input("🧠 **IQ**", min_value=50, max_value=140, value=110, help="Enter the student's IQ score.")

        # Column 2: Academic Information
        with col2:
            
            course_level = st.selectbox("📈 **Course Level**", ["Low", "Medium", "High"], help="Select the course difficulty level.")
            material_level = st.selectbox("📒 **Material Level**", ["Low", "Medium", "High"], help="Select the material difficulty level.")
            previous_scores = st.number_input("📊 **Previous Scores**", min_value=0, max_value=100, value=75, help="Enter the student's previous scores.")

        # Column 3: Cognitive and Behavioral Information
        with col3:
           
            assessment_score = st.number_input("📝 **Assessment Score**", min_value=0, max_value=100, value=85, help="Enter the student's assessment score.")
            attendance = st.number_input("📅 **Attendance (%)**", min_value=0.0, max_value=100.0, value=90.0, help="Enter the student's attendance percentage.")
            study_time = st.number_input("⏱️ **Study Time**", min_value=0.0, max_value=10.0, value=6.0, help="Enter the student's daily study time in hours.")

        # Centered Submit Button
        st.markdown(
            """
            <div style="text-align: center;">
                <br>
            </div>
            """,
            unsafe_allow_html=True
        )
        submitted = st.form_submit_button("🔮 **Predict & Recommend**")

# ---- PREDICT BUTTON ----
if submitted:
    # Prepare input data
    input_data = pd.DataFrame({
        "Age": [age],
        "Level": [level],
        "Course Level": [course_level],
        "Material Level": [material_level],
        "Previous_Scores": [previous_scores],
        "Assesment Score": [assessment_score],
        "IQ": [iq],
        "Attendance": [attendance],
        "Study Time": [study_time]
    })

    try:
        # Make Prediction
        prediction = pipeline.predict(input_data)

        # ---- SHOW RECOMMENDATIONS ----
        st.subheader("📚 **Recommended Learning Resources:**")

        resources = recommended_material.get(prediction[0], [])

        if resources:
            # Display resources in a structured layout
            cols = st.columns(len(resources))  # Create columns for card layout
            for idx, resource in enumerate(resources):
                with cols[idx]:
                    st.markdown(
                        f"""
                        <div class="card">
                            <h3>{resource['name']}</h3>
                            <p>{resource['description']}</p>
                            <a href="{resource['link']}" target="_blank">🔗 Visit Resource</a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            st.warning("⚠️ No resources found for this level.")

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")

# ---- FOOTER ----
st.markdown(
    """
    <div class="footer">
        🎓 Developed by <a href="https://www.linkedin.com/in/atanu-guchhait-4a6427296/" target="_blank">Atanu</a> | © 2025
    </div>
    """,
    unsafe_allow_html=True
)
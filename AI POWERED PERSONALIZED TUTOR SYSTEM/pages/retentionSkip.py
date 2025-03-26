import streamlit as st
import pandas as pd
import pickle

# Custom CSS for black text, white background, and styled recommendations
st.markdown(
    """
    <style>
        body, .stApp, .stTextInput label, .stSelectbox label, .stButton, .stSuccess, .stError, 
        h1, h2, h3, h4, h5, h6, .stMarkdown, .stTitle, .stHeader, .stText, .stAlert p, .stAlert h1, .stAlert h2 {
            background-color: white !important;
            color: black !important;
        }
        .stButton>button {
            background-color: #007BFF;  /* Blue button */
            color: white !important;
            font-weight: bold;
        }
        .stSuccess, .stError {
            background-color: #d4edda !important;  /* Greenish background */
            color: black !important;
            font-weight: bold;
        }
        .stAlert p, .stAlert h1, .stAlert h2 {
            color: black !important;  /* Black text in alerts */
        }
        .recommendation {
            font-size: 22px !important;   /* Increased font size */
            font-weight: bold;
            color: #333;                   /* Dark grey for contrast */
            background: #f1f1f1;           /* Light grey background */
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin: 20px 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the trained model from the .pkl file
@st.cache_resource
def load_model():
    with open("skipRetention.pkl", "rb") as f:   # Replace with your actual .pkl file name
        pipeline = pickle.load(f)
    return pipeline

# Load the model
pipeline = load_model()

# Labels for recommendations (updated as per your request)
y = [
    'Textbooks, Workbooks, Educational Apps, Science Kits',                # y[0] -> Elementary
    'Reference Books, Online Courses, Project Kits, Lab Manuals',          # y[1] -> Middle School
    'Storybooks, Flashcards, Interactive Games, Coloring Sheets',          # y[2] -> Kindergarten
    'Advanced Textbooks, Research Papers, Online Certifications, Programming Tutorials'  # y[3] -> High School
]

# Streamlit app layout
st.title("📚 RETENTION/SKIPPED CONTENT AS PER STUDENT LEVEL")
st.write("### Enter the student level to get personalized learning resources")

# User input
level = st.selectbox(
    "Select Student Level:", 
    ['Kindergarten', 'Elementary', 'Middle School', 'High School']
)

# Function to reshape input properly
def reshape_input(level):
    """Ensures consistent 2D input format for model"""
    return pd.DataFrame([[level]])

# Make prediction
if st.button("Get Content"):
    input_data = reshape_input(level)

    # Perform prediction with error handling
    try:
        prediction = pipeline.predict(input_data)

        # Recommendation function with corrected mapping
        def recommend(n):
            if n == 0:
                return y[3]   # Elementary
            elif n == 1:
                return y[1]   # Middle School
            elif n == 2:
                return y[2]   # Kindergarten
            elif n == 3:
                return y[0]   # High School
            else:
                return "No recommendation available."

        # Display recommendation
        st.success("✅ **Kindly Follow These Resources:**")
        
        # Styled recommendation with larger font size
        st.markdown(
            f"<div class='recommendation'>{recommend(prediction[0])}</div>",
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.write("⚠️ Please check the input format or model compatibility.")

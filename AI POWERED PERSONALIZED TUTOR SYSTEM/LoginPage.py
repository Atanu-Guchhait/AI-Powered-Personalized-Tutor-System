import streamlit as st

# Page Configuration - Full Screen Mode
st.set_page_config(page_title="Student Login", page_icon="🎓", layout="wide")

# Custom CSS for Full-Screen Mode
st.markdown(
    """
    <style>
        /* Hide top-left empty box */
        [data-testid="stDecoration"] { display: none; }
        
        /* Remove unnecessary padding */
        .block-container { padding: 0px !important; margin: 0px !important; width: 100vw; height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; }
        
        /* Full-Screen Background */
        .stApp { background: linear-gradient(135deg, #1A1A2E, #16213E); color: white; }
        
        /* Centered Login Title */
        .login-title { text-align: center; color: #00FFF5; font-size: 40px; font-weight: bold; margin-bottom: 20px; }
        
        /* Styled Form */
        .st-form { background: rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0, 255, 245, 0.3); width: 50%; text-align: center; }
        
        /* Styled Buttons */
        .stButton>button { background: linear-gradient(135deg, #00FFF5, #0077B6); color: white; font-size: 18px; padding: 15px; border-radius: 8px; width: 100%; transition: all 0.3s ease-in-out; }
        .stButton>button:hover { background: linear-gradient(135deg, #0077B6, #00FFF5); transform: scale(1.05); }
        
        /* Dashboard Title */
        .dashboard-title { text-align: center; font-size: 40px; font-weight: bold; color: #00FFF5; margin-top: 20px; }
        
        /* Dashboard Box Layout */
        .dashboard-container { display: flex; justify-content: center; align-items: center; gap: 40px; flex-wrap: wrap; width: 100%; margin-top: 30px; }
        
        /* Dashboard Box Styling */
        .box { background: rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 15px rgba(0, 255, 245, 0.3); font-size: 22px; font-weight: bold; color: white; width: 300px; cursor: pointer; transition: 0.3s ease-in-out; }
        .box:hover { background: rgba(0, 255, 245, 0.3); transform: scale(1.05); box-shadow: 0px 6px 20px rgba(0, 255, 245, 0.6); }
    </style>
    """,
    unsafe_allow_html=True
)

# **Session State for Page Navigation**
if "page" not in st.session_state:
    st.session_state.page = "login"

# **Login Page**
if st.session_state.page == "login":
    st.markdown('<h1 class="login-title">🎓 Student Login</h1>', unsafe_allow_html=True)

    with st.form("login_form"):
        name = st.text_input("🧑 Name", placeholder="Enter your full name")
        age = st.number_input("📅 Age", min_value=3, max_value=18, step=1)
        level = st.selectbox("🏫 Level", ["Kindergarten", "Elementary", "Middle School", "High School"])
        email = st.text_input("📧 Email ID", placeholder="Enter your email")

        submitted = st.form_submit_button("🔓 Login")

        if submitted:
            if not name or not email:
                st.warning("⚠️ Please enter your name and email to continue!")
            else:
                st.session_state.page = "dashboard"
                st.session_state.user = {"name": name, "age": age, "level": level, "email": email}
                st.rerun()

# **Dashboard Page**
elif st.session_state.page == "dashboard":
    st.markdown('<h1 class="dashboard-title">📊 Student Dashboard</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📈 Predict Assessment Score", use_container_width=True):
            st.switch_page("pages/PredictAssesmentScore.py")

        if st.button("📚 Recommendation", use_container_width=True):
            st.info("📖 AI will suggest the best learning materials!")
            st.switch_page("pages/Recommendation.py")

        if st.button("🔍 Retention Analysis", use_container_width=True):
            st.switch_page("pages/retentionSkip.py")

    with col2:
        if st.button("🎓 Check Promotion", key="check_promotion", use_container_width=True):
            st.switch_page("pages/Promotion.py")
        
        if st.button("📦 Doubt", use_container_width=True):
            st.switch_page("pages/PdfQuery.py")

        # ✅ Added retentionSkip.py page
        if st.button("EDA", use_container_width=True):
            st.switch_page("pages\EDA.py")
            
    # Logout Button
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()

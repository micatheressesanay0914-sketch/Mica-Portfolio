import streamlit as st

st.set_page_config(
    page_title="Mica Portfolio",
    page_icon="💼",
    layout="wide"
)

# ------------------ SIDEBAR ------------------
page = st.sidebar.radio(
    "Navigation",
    ["Home", "About", "Skills", "Projects", "Contact"]
)

# ------------------ CSS ------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap');

.stApp {
    background: linear-gradient(-45deg, #141e30, #243b55, #1f1c2c, #2c3e50);
    background-size: 400% 400%;
    animation: bgMove 18s ease infinite;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.banner-wrapper {
    width: 90%;
    max-width: 900px;
    margin: 70px auto;
    padding: 60px 30px;
    border-radius: 25px;
    text-align: center;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    box-shadow: 0 25px 70px rgba(0,0,0,0.5);
    animation: fadeIn 1.2s ease;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(40px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes floatText {
    0% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0);}
}

.banner-headline {
    font-size: 70px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    animation: floatText 3s ease-in-out infinite;
}

.intro {
    max-width: 750px;
    margin: auto;
    text-align: center;
    color: #e0e0e0;
    font-size: 18px;
    line-height: 1.8;
    margin-top: 40px;
}

.highlight {
    color: #ffb199;
    font-weight: bold;
}

@media (max-width: 768px) {
    .banner-headline {
        font-size: 45px;
    }
}

</style>
""", unsafe_allow_html=True)

# ------------------ HOME ------------------
if page == "Home":

    st.markdown("""
    <div class="banner-wrapper">
        <div class="banner-headline">
            Mica Portfolio
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='intro'>
    Hello! I am a <span class='highlight'>BS Computer Science student</span> passionate about building modern applications.

    Explore my background, skills, and projects using the sidebar.
    </div>
    """, unsafe_allow_html=True)

# ------------------ ABOUT ------------------
elif page == "About":

    st.title("About Me 💡")

    st.write("""
    I am a Computer Science student focused on:
    - Web Development
    - UI/UX Design
    - Python Applications
    - Learning modern frameworks

    I enjoy building clean and functional systems.
    """)

# ------------------ SKILLS ------------------
elif page == "Skills":

    st.title("Skills 🧠")

    st.write("""
    - Python 🐍  
    - Streamlit 🌐  
    - HTML & CSS 🎨  
    - Basic JavaScript ⚡  
    - UI/UX Design 🎯  
    - Problem Solving 🧩  
    """)

# ------------------ PROJECTS ------------------
elif page == "Projects":

    st.title("Projects 🚀")

    st.write("""
    **1. Portfolio Website (Streamlit)**  
    A modern animated portfolio built with Python.

    **2. Student Management System**  
    A CRUD system using Python.

    **3. Simple AI Chatbot**  
    Basic chatbot using rule-based logic.
    """)

# ------------------ CONTACT ------------------
elif page == "Contact":

    st.title("Contact Me 📬")

    st.write("""
    📧 Email: mica@example.com  
    💻 GitHub: github.com/mica  
    🔗 LinkedIn: linkedin.com/in/mica  
    """)

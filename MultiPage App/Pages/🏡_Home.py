import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Mica Portfolio",
    page_icon="🏡",
    layout="wide"
)

# ---------- IMAGE TO BASE64 (SAFE LOADING) ----------
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# ✅ OS FIX ADDED HERE
BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "me", "Image.jpg")

img_base64 = get_base64_image(img_path)

# ---------- CSS ----------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap');

/* BACKGROUND */
.stApp {
    background: linear-gradient(-45deg, #141e30, #243b55, #1f1c2c, #2c3e50);
    background-size: 400% 400%;
    animation: bgMove 18s ease infinite;
}

/* BACKGROUND ANIMATION */
@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* TITLE */
.title {
    text-align: center;
    font-size: 70px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    margin-top: 50px;
    animation: floatText 3s ease-in-out infinite;
}

/* FLOAT ANIMATION */
@keyframes floatText {
    0% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0);}
}

/* PROFILE CARD */
.card {
    width: 320px;
    margin: 40px auto;
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    transition: 0.4s ease;
    animation: fadeIn 1.5s ease;
}

/* HOVER EFFECT */
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px #ffb199, 0 0 50px #ff4d6d;
}

/* PROFILE IMAGE WITH GLOW */
.profile-pic {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #ffb199;
    box-shadow: 0 0 20px #ffb199, 0 0 40px #ff4d6d;
    margin-bottom: 15px;
}

/* NAME */
.card h2 {
    color: white;
    margin: 10px 0;
}

/* SUMMARY */
.summary {
    max-width: 750px;
    margin: 40px auto;
    text-align: justify;
    text-justify: inter-word;
    color: #e0e0e0;
    font-size: 18px;
    line-height: 1.9;
    padding: 0 20px;
    animation: fadeIn 2s ease;
}

/* HIGHLIGHT TEXT */
.highlight {
    color: #ffb199;
    font-weight: bold;
}

/* FADE ANIMATION */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .title {
        font-size: 45px;
    }

    .card {
        width: 85%;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("""
<div class="title">
Mica Portfolio
</div>
""", unsafe_allow_html=True)

# ---------- PROFILE CARD ----------
st.markdown(f"""
<div class="card">
    <img class="profile-pic" src="data:image/jpg;base64,{img_base64}">
    <h2>Mica</h2>
    <p style="color:#ccc;">BS Computer Science Student</p>
</div>
""", unsafe_allow_html=True)

# ---------- SUMMARY ----------
st.markdown("""
<div class="summary">
Hello! I am <span class="highlight">Mica</span>, a passionate BS Computer Science student focused on building modern web applications and creative UI designs.

I enjoy learning Python, web development, and exploring new technologies that improve user experience and design.

My goal is to become a skilled developer who creates meaningful and functional digital solutions.
</div>
""", unsafe_allow_html=True)

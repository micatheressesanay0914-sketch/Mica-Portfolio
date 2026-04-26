import streamlit as st
import base64
import os

# ---------- IMAGE TO BASE64 ----------
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# ---------- SAFE PATH USING OS ----------
BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "me", "Image.jpg")

img_base64 = get_base64_image(img_path)

# ---------- TITLE ----------
st.markdown("""
<div style="
text-align:center;
font-size:70px;
font-weight:900;
color:white;
font-family:'Barlow Condensed', sans-serif;
margin-top:50px;
">
Mica Portfolio
</div>
""", unsafe_allow_html=True)

# ---------- PROFILE CARD ----------
st.markdown(f"""
<div style="
width:320px;
margin:40px auto;
background:rgba(255,255,255,0.10);
backdrop-filter:blur(10px);
border-radius:20px;
padding:25px;
text-align:center;
box-shadow:0 15px 40px rgba(0,0,0,0.4);
">
    <img src="data:image/jpg;base64,{img_base64}" 
    style="
        width:140px;
        height:140px;
        border-radius:50%;
        object-fit:cover;
        border:4px solid #ffb199;
        box-shadow:0 0 20px #ffb199;
    ">
    
    <h2 style="color:white;">Mica</h2>
    <p style="color:#ccc;">BS Computer Science Student</p>
</div>
""", unsafe_allow_html=True)

# ---------- SUMMARY ----------
st.markdown("""
<div style="
max-width:750px;
margin:40px auto;
text-align:justify;
color:#e0e0e0;
font-size:18px;
line-height:1.9;
padding:0 20px;
">

Hello! I am <b style="color:#ffb199;">Mica</b>, a passionate BS Computer Science student focused on building modern web applications and creative UI designs.

I enjoy learning Python, web development, and exploring new technologies that improve user experience and design.

My goal is to become a skilled developer who creates meaningful and functional digital solutions.

</div>
""", unsafe_allow_html=True)

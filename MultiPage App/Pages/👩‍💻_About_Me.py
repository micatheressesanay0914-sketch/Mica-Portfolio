import streamlit as st
import base64

    page_title="About Me - Mica",
    page_icon="👤",
    layout="wide"

# ---------- IMAGE TO BASE64 ----------
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

cert1 = img_to_base64("Pages/me/cert1.jpg")
cert2 = img_to_base64("Pages/me/cert2.jpg")

# ---------- STYLE ----------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap');

/* BACKGROUND */
.stApp {
    background: linear-gradient(-45deg, #141e30, #243b55, #1f1c2c, #2c3e50);
    background-size: 400% 400%;
    animation: bgMove 18s ease infinite;
    font-family: 'Barlow', sans-serif;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* TITLE */
.title {
    text-align: center;
    font-size: 60px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    margin-top: 50px;
}

/* ABOUT CARD */
.card {
    max-width: 850px;
    margin: 50px auto;
    padding: 40px;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.info {
    color: #e0e0e0;
    font-size: 17px;
    line-height: 1.8;
}

h3 {
    color: #ffb199;
}

/* CERT TITLE */
.cert-title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin-top: 70px;
    margin-bottom: 20px;
}

/* CERT GRID */
.cert-grid {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 50px;
    margin-top: 20px;
}

/* CERT CARD (BIG + PREMIUM) */
.cert-card {
    width: 520px;
    height: 320px;
    border-radius: 18px;
    overflow: hidden;
    position: relative;
    cursor: pointer;
    transition: 0.5s ease;
    box-shadow: 0 15px 35px rgba(0,0,0,0.5);
}

/* IMAGE */
.cert-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: 0.5s ease;
}

/* HOVER (3D + GLOW + LIFT) */
.cert-card:hover {
    transform: translateY(-18px) scale(1.08) rotateX(4deg);
    box-shadow: 
        0 0 30px #ff4d6d,
        0 0 80px #ffb199,
        0 30px 90px rgba(0,0,0,0.6);
}

.cert-card:hover img {
    transform: scale(1.15);
    filter: brightness(1.3) contrast(1.1);
}

/* TEXT */
.cert-text {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 10px;
    text-align: center;
    background: rgba(0,0,0,0.65);
    color: white;
    font-weight: bold;
    font-size: 15px;
}

/* EXPANDER (CLICK VIEW FULL IMAGE) */
details {
    text-align: center;
    color: white;
    margin-top: 10px;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .title { font-size: 40px; }

    .cert-card {
        width: 95%;
        height: 240px;
    }

    .cert-grid {
        gap: 25px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">👤 About Me</div>', unsafe_allow_html=True)

# ---------- ABOUT ----------
st.markdown("""
<div class="card">
    <div class="info">
        <h3>Hi! I'm Mica 👋</h3>
        <p>A BS Computer Science student passionate about programming 💻 and building modern applications.</p>
        <h3>📋 Basic Information</h3>
        <p>Name: Mica Theresse Sanay<br>Course: BS Computer Science</p>
        <h3>🎯 Goals</h3>
        <p>• Become a Full Stack Developer<br>• Build impactful tech solutions</p>
        <h3>🎮 Hobbies</h3>
        <p>• Watching Asian Dramas<br>• Reading Novels<br>• Sleeping 😴</p>
    </div>
</div>
""", unsafe_allow_html=True)
# ---------- CERTIFICATES ----------
st.markdown('<div class="cert-title">🏆 Certificates</div>', unsafe_allow_html=True)

# CERT 1 (TOP)
st.markdown(f"""
<div class="cert-grid">
    <div class="cert-card">
        <img src="data:image/jpg;base64,{cert1}">
        <div class="cert-text">Cisco Certificate</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

with st.expander("🔍 View Certificate 1"):
    st.image("Pages/me/cert1.jpg", use_container_width=True)

# CERT 2 (BOTTOM)
st.markdown(f"""
<div class="cert-grid">
    <div class="cert-card">
        <img src="data:image/jpg;base64,{cert2}">
        <div class="cert-text">Simplilearn Certificate</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

with st.expander("🔍 View Certificate 2"):
    st.image("Pages/me/cert2.jpg", use_container_width=True)

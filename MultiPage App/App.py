import streamlit as st

st.set_page_config(
    page_title="Mica Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap');

/* BACKGROUND */
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

/* HERO BOX */
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
}

/* TITLE */
.banner-headline {
    font-size: 70px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
}

/* INTRO */
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

/* RESPONSIVE */
@media (max-width: 768px) {
    .banner-headline {
        font-size: 45px;
    }
}

/* ===== GITHUB FORK RIBBON ===== */
.github-corner {
  position: fixed;
  top: 0;
  right: 0;
  z-index: 9999;
}

.github-corner svg {
  fill: #ff4d6d;
  color: #fff;
  width: 80px;
  height: 80px;
  transition: 0.3s ease;
}

.github-corner:hover svg {
  transform: scale(1.1);
  fill: #ffb199;
}

</style>
""", unsafe_allow_html=True)

# ------------------ GITHUB FORK BUTTON ------------------
st.markdown("""
<a href="https://github.com/" target="_blank" class="github-corner" aria-label="View source on GitHub">
<svg viewBox="0 0 250 250">
    <path d="M0,0 L250,250 L250,0 Z"></path>
</svg>
</a>
""", unsafe_allow_html=True)

# ------------------ HERO ------------------
st.markdown("""
<div class="banner-wrapper">
    <div class="banner-headline">
        Mica Portfolio
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------ INTRO ------------------
st.markdown("""
<div class='intro'>
Hello! I am a <span class='highlight'>BS Computer Science student</span> passionate about building modern applications and exploring new technologies.
</div>
""", unsafe_allow_html=True)

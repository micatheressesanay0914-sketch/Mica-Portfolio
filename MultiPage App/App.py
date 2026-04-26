import streamlit as st

st.set_page_config(
    page_title="Mica Portfolio",
    page_icon="💼",
    layout="wide"
)

# ---------- SIDEBAR ----------
menu = st.sidebar.radio(
    "📌 Navigation",
    ["Home", "About Me", "Projects", "Skills", "Contact"]
)

# ---------- CSS (UNCHANGED) ----------
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

.banner-headline {
    font-size: 70px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    animation: floatText 3s ease-in-out infinite;
}

@keyframes floatText {
    0% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0);}
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

# ---------- HOME ----------
if menu == "Home":
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

    I enjoy designing clean UI and developing functional systems using Python and web technologies.
    </div>
    """, unsafe_allow_html=True)

# ---------- OTHER PAGES (FIXED) ----------
elif menu == "About Me":
    with open("about_me.py", "r", encoding="utf-8") as f:
        exec(f.read())

elif menu == "Projects":
    with open("project.py", "r", encoding="utf-8") as f:
        exec(f.read())

elif menu == "Skills":
    with open("skills.py", "r", encoding="utf-8") as f:
        exec(f.read())

elif menu == "Contact":
    with open("contact.py", "r", encoding="utf-8") as f:
        exec(f.read())

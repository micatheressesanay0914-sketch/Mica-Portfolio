import streamlit as st

st.set_page_config(
    page_title="Mica Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to:",
    ["Home", "About", "Skills", "Projects", "Contact"]
)

# ---------------- GITHUB FORK BUTTON ----------------
st.markdown("""
<a href="https://github.com/your-repo-link" target="_blank">
<button style="
position: fixed;
top: 15px;
right: 15px;
padding: 10px 15px;
background: linear-gradient(135deg, #ff4d6d, #ffb199);
color: white;
border: none;
border-radius: 12px;
font-weight: bold;
cursor: pointer;
z-index: 9999;
box-shadow: 0 10px 25px rgba(0,0,0,0.4);
">
⭐ Fork on GitHub
</button>
</a>
""", unsafe_allow_html=True)

# ---------------- STYLE ----------------
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
    animation: fadeIn 1.2s ease;
}

/* FADE */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(40px);}
    to {opacity: 1; transform: translateY(0);}
}

/* FLOAT TITLE */
@keyframes floatText {
    0% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0);}
}

/* TITLE */
.banner-headline {
    font-size: 70px;
    font-weight: 900;
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    animation: floatText 3s ease-in-out infinite;
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

</style>
""", unsafe_allow_html=True)

# ---------------- PAGES ----------------
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
    Hello! I am a <span class='highlight'>BS Computer Science student</span> passionate about building modern applications and exploring new technologies.

    I enjoy designing clean user interfaces and developing functional systems using Python and web technologies.

    Feel free to explore my portfolio and see my work.
    </div>
    """, unsafe_allow_html=True)

elif page == "About":
    st.title("👤 About Me Page")

elif page == "Skills":
    st.title("🧠 Skills Page")

elif page == "Projects":
    st.title("💻 Projects Page")

elif page == "Contact":
    st.title("📞 Contact Page")

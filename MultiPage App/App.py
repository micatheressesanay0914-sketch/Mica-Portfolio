import streamlit as st

st.set_page_config(
    page_title="Mica Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- FIXED FORK RIBBON ----------------
st.markdown("""
<style>

/* FORCE APP VISIBILITY */
[data-testid="stAppViewContainer"] {
    overflow: visible !important;
}

/* FORK RIBBON */
.fork-ribbon {
    position: fixed;
    top: 20px;
    right: -55px;
    z-index: 999999;
    transform: rotate(45deg);
    background: linear-gradient(135deg, #ff4d6d, #ffb199);
    color: white;
    padding: 10px 70px;
    font-size: 12px;
    font-weight: bold;
    text-decoration: none;
    box-shadow: 0 10px 25px rgba(0,0,0,0.6);
    border-radius: 6px;
}

.fork-ribbon:hover {
    transform: rotate(45deg) scale(1.08);
    transition: 0.3s ease;
}

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

/* HERO */
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

.banner-headline {
    font-size: 70px;
    font-weight: 900;
    color: white;
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

</style>

<a class="fork-ribbon"
   href="https://github.com/YOUR-USERNAME/YOUR-REPO"
   target="_blank">
   Fork on GitHub
</a>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR (FORCED CONTENT) ----------------
with st.sidebar:
    st.title("📂 Navigation")
    page = st.radio("Go to:", ["Home", "About", "Skills", "Projects", "Contact"])

    st.markdown("---")
    st.write("💼 Mica Portfolio")
    st.write("Built with Streamlit")

# ---------------- HOME ----------------
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
    </div>
    """, unsafe_allow_html=True)

elif page == "About":
    st.title("👤 About Me")

elif page == "Skills":
    st.title("🧠 Skills")

elif page == "Projects":
    st.title("💻 Projects")

elif page == "Contact":
    st.title("📞 Contact")

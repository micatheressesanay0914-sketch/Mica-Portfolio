import streamlit as st

st.set_page_config(
    page_title="Mica Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- FIX: UNHIDE FORK ----------------
st.markdown("""
<style>

/* 🔥 FORCE STREAMLIT LAYERS TO NOT COVER RIBBON */
html, body, [data-testid="stAppViewContainer"] {
    overflow: visible !important;
}

/* 🔥 ROOT LAYER FIX */
[data-testid="stAppViewContainer"] > .main {
    overflow: visible !important;
}

/* 🔥 FORK RIBBON */
.fork-ribbon {
    position: fixed;
    top: 25px;
    right: -55px;
    z-index: 9999999999 !important;
    transform: rotate(45deg);
    background: linear-gradient(135deg, #ff4d6d, #ffb199);
    color: white;
    padding: 10px 70px;
    font-size: 12px;
    font-weight: bold;
    text-decoration: none;
    border-radius: 6px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.6);
}

/* hover */
.fork-ribbon:hover {
    transform: rotate(45deg) scale(1.08);
    transition: 0.3s ease;
}

</style>

<a class="fork-ribbon"
   href="https://github.com/YOUR-USERNAME/YOUR-REPO"
   target="_blank">
   Fork on GitHub
</a>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR (FORCED) ----------------
with st.sidebar:
    st.title("📂 Navigation")
    page = st.radio("Go to:", ["Home", "About", "Skills", "Projects", "Contact"])

# ---------------- MAIN ----------------
if page == "Home":
    st.title("Mica Portfolio")
    st.write("Welcome to my portfolio 🚀")

elif page == "About":
    st.title("About Me")

elif page == "Skills":
    st.title("Skills")

elif page == "Projects":
    st.title("Projects")

elif page == "Contact":
    st.title("Contact")

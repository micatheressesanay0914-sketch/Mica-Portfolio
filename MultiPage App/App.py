import streamlit as st

st.set_page_config(
    page_title="Mica Portfolio",
    page_icon="💼",
    layout="wide"
)

# ------------------ CSS ------------------
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
    font-family: 'Barlow Condensed', sans-serif;
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

</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "About", "Projects", "Skills", "Contact"]
)

# ------------------ HOME ------------------
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
    Hello! I am a <span class='highlight'>BS Computer Science student</span> passionate about building modern applications and exploring new technologies.

    I enjoy designing clean user interfaces and developing functional systems using Python and web technologies.

    Feel free to explore my portfolio and see my work.
    </div>
    """, unsafe_allow_html=True)

# ------------------ ABOUT ------------------
elif menu == "About":
    st.title("About Me")
    st.write("""
    I am a Computer Science student focused on software development, UI design, and web applications.
    I enjoy learning new frameworks and improving my programming skills.
    """)

# ------------------ PROJECTS ------------------
elif menu == "Projects":
    st.title("Projects")

    st.subheader("Portfolio Website")
    st.write("A personal portfolio built using Streamlit.")

    st.subheader("Other Project")
    st.write("You can add more projects here.")

# ------------------ SKILLS ------------------
elif menu == "Skills":
    st.title("Skills")

    st.write("💻 Python")
    st.write("🌐 HTML / CSS")
    st.write("⚡ Streamlit")
    st.write("🎨 UI Design")

# ------------------ CONTACT ------------------
elif menu == "Contact":
    st.title("Contact Me")

    st.write("📧 Email: yourname@email.com")
    st.write("📍 Location: Philippines")
    st.write("💼 Open for internship opportunities")

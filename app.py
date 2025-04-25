import streamlit as st

# Page config
st.set_page_config(page_title="Happy Birthday Harshhh", page_icon="🦄", layout="centered")

# CSS for full pink background and stylish white glowing text
page_style = """
<style>
body {
    background-color: #ff99bb;
    margin: 0;
    padding: 0;
}

h1, h2, p, div, footer {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
    text-align: center;
    text-shadow: 2px 2px 6px #ff66a3;
}

h1 {
    font-size: 3.5rem;
    margin-top: 30px;
}

h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

p {
    font-size: 1.3rem;
    line-height: 1.6;
}

footer {
    font-size: 1rem;
    margin-top: 2rem;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Title
st.markdown("<h1>💖 harshhh 🦄 💖</h1>", unsafe_allow_html=True)

# Birthday message box (still centered and clean)
st.markdown("""
<div style="padding: 2rem;">
    <h2>Happy Birthday to my payri beautiful best friend harshhh!</h2>
    <p>
        Teri har ek smile duniya ko bright karti hai!<br/>
        Tu sirf meri best friend nahi hai, tu meri soul sister hai.<br/><br/>
        Aaj ka din sirf tera hai... khub hasi, khub khushiyan, aur dher sara pyaar milay tujhe.<br/>
        Tere bina meri life kaafi boring hoti... tu hai toh sab kuch hai!<br/><br/>
        Hamesha aise hi mast rehna, khush rehna aur mujhe ignore mat karna!<br/><br/>
        harshhh, tujhe sab kuch best mile zindagi me!<br/>
    </p>
</div>
""", unsafe_allow_html=True)

# Confetti blast 🎉
st.balloons()

# Footer
st.markdown("<hr style='border: 1px solid white;'>", unsafe_allow_html=True)
st.markdown("<footer>made by mani to harshhh with 💖</footer>", unsafe_allow_html=True)

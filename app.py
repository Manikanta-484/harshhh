import streamlit as st
import time

# Set page config
st.set_page_config(page_title="Happy Birthday Harshhh", page_icon="🦄", layout="centered")

# Background color using custom CSS
page_bg = """
<style>
body {
background-color: #ffccda;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Unicorn title
st.markdown("<h1 style='text-align: center; color: white; font-size: 3rem;'>harshhh 🦄</h1>", unsafe_allow_html=True)

# Birthday message
st.markdown("""
<div style="background-color: #ffccda; padding: 2rem; border-radius: 10px; text-align: center; color: white; font-size: 1.2rem;">
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

# Confetti 🎉🎉
st.balloons()

# Footer
st.markdown("<br><br><hr style='border: 1px solid white;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: white;'>made by mani to harshhh</div>", unsafe_allow_html=True)

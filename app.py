import streamlit as st

# Set page config
st.set_page_config(page_title="Happy Birthday Harshhh", page_icon="🦄", layout="centered")

# Darker pink full-page background using CSS
page_bg = """
<style>
body {
background-color: #ff99bb; /* little darker pink */
margin: 0;
padding: 0;
}
h1 {
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
font-size: 3.5rem;
color: white;
text-shadow: 2px 2px 5px #ff66a3; /* cute shadow effect */
margin-top: 30px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Unicorn fancy title
st.markdown("<h1 style='text-align: center;'>💖 harshhh 🦄 💖</h1>", unsafe_allow_html=True)

# Birthday message
st.markdown("""
<div style="padding: 2rem; border-radius: 15px; text-align: center; color: white; font-size: 1.3rem;">
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

# Confetti blast 🎉🎉
st.balloons()

# Footer
st.markdown("<br><br><hr style='border: 1px solid white;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: white; font-size: 1rem;'>made by mani to harshhh with 💖</div>", unsafe_allow_html=True)

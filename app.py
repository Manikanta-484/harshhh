import streamlit as st

# Page config
st.set_page_config(page_title="Happy Birthday Harshhh", page_icon="🦄", layout="centered")

# CSS styling
page_style = """
<style>
body {
    background-color: #87ceeb;
    margin: 0;
    padding: 0;
}

/* Only special style for the unicorn heading */
h1 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
    text-align: center;
    text-shadow: 2px 2px 6px #ff66a3;
    font-size: 3.5rem;
    margin-top: 30px;
}

/* Regular text styling */
h2, p, footer {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
    text-align: center;
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

# Special unicorn heading
st.markdown("<h1>💖 harshhh 🦄 💖</h1>", unsafe_allow_html=True)

# Birthday message
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

# Confetti 🎉

import streamlit as st

# Page config
st.set_page_config(page_title="Happy Birthday Harshhh", page_icon="🦄", layout="centered")

# CSS styling
page_style = """
<style>
body {
    background-color: #87ceeb;
    background-image: url("https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    margin: 0;
    padding: 0;
}

/* Unicorn heading */
h1 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
    text-align: center;
    text-shadow: 2px 2px 6px #ff66a3;
    font-size: 3.5rem;
    margin-top: 30px;
}

/* Birthday wish text */
h2 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
    text-align: center;
    background-color: #FFC0CB;
    font-size: 2rem;
    margin-bottom: 1rem;
}

p {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: black;
    text-align: center;
    font-size: 1.3rem;
    line-height: 1.7;
    background-color: #FFC0CB;
    padding: 1rem;
    # border-radius: 10px;
    margin: 0 auto;
    max-width: 600px;
}

/* Footer */
footer {
    background-color: #4682b4;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    text-align: center;
    padding: 1rem;
    font-size: 1.1rem;
    border-top: 2px solid white;
    margin-top: 2rem;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Unicorn heading
st.markdown("<h1>💖 harshhh 🦄 💖</h1>", unsafe_allow_html=True)

# Birthday message
st.markdown("""
<h2>Happy Birthday to my payri beautiful best friend harshhh!</h2>
<p>
    Teri har ek smile duniya ko bright karti hai!<br/>
    Tu sirf meri best friend nahi hai, tu meri soul sister hai.<br/><br/>
    Aaj ka din sirf tera hai... khub hasi, khub khushiyan, aur dher sara pyaar milay tujhe.<br/>
    Tere bina meri life kaafi boring hoti... tu hai toh sab kuch hai!<br/><br/>
    Hamesha aise hi mast rehna, khush rehna aur mujhe ignore mat karna!<br/><br/>
    harshhh, tujhe sab kuch best mile zindagi me!<br/>
</p>
""", unsafe_allow_html=True)

# Confetti 🎉
st.balloons()

# Footer
st.markdown("<footer>From Mani #soyabean </footer>", unsafe_allow_html=True)

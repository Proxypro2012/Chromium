import streamlit as st
import streamlit.components.v1 as components

# Title of the web app
st.title("Chromium")
st.write("Versatile web proxy. For my guys at school.")

# Game URLs dictionary
game_urls = {
    "getaway_shootout": "https://selenite.cc/semag/getawayshooter/index.html"
}

# Try embedding the game in an iframe
st.subheader("Embedded Game (May not work due to security restrictions)")
try:
    components.iframe(game_urls["getaway_shootout"], width=1500, height=700)
except:
    st.error("Sorry guys, looks like this game just got blocked :(")

# Alternative option: Provide a clickable link
st.subheader("Alternative Link")
st.markdown(f'[Click here to play Getaway Shooter]({game_urls["getaway_shootout"]})', unsafe_allow_html=True)

# Additional app features
st.text("Enjoy playing Getaway Shooter!")

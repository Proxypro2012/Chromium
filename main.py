import streamlit as st
import streamlit.components.v1 as components

# Title of the web app
st.title("Play Getaway Shooter Game")

# Game URL to be embedded
game_url = "https://selenite.cc/semag/getawayshooter/index.html"

# Try embedding the game in an iframe
st.subheader("Embedded Game (May not work due to security restrictions)")
try:
    components.iframe(game_url, width=400, height=300)
except:
    st.error("Embedding failed. Use the link below to play the game.")

# Alternative option: Provide a clickable link
st.subheader("Alternative Link")
st.markdown(f'[Click here to play Getaway Shooter]({game_url})', unsafe_allow_html=True)

# Additional app features
st.text("Enjoy playing Getaway Shooter!")

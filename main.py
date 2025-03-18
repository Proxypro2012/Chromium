import streamlit as st
import streamlit.components.v1 as components

# Title of the web app
st.title("Play Getaway Shooter Game")

# Game URL to be embedded
game_url = "https://selenite.cc/semag/getawayshooter/index.html"

# Embed the game in an iframe
components.iframe(game_url, width=800, height=600)

# Additional app features
st.text("Enjoy playing Getaway Shooter!")

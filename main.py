import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")


game_urls = {
    "getaway_shootout": "https://selenite.cc/semag/getawayshooter/index.html"
}


webpages = ["Home", "Games", "PictureOfTheDay"]
selected_page = st.sidebar.radio("Navigation", webpages)




if selected_page == webpages[0]:
    st.title("Chromium")
    st.write("Versatile web proxy. For my guys at school.")




    
    
if selected_page == webpages[1]:
    st.subheader("Getaway Shootout!")
    try:
        components.iframe(game_urls["getaway_shootout"], width=800, height=625)
    except:
        st.error("Embedding failed. Use the link below to play the game.")
    
    # Alternative option: Provide a clickable link
    st.subheader("Alternative Link")
    st.markdown(f'[Click here to play Getaway Shootout]({game_urls["getaway_shootout"]})', unsafe_allow_html=True)
    
    # Additional app features
    st.text("Enjoy playing Getaway Shootout!")

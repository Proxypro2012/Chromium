import streamlit as st
import streamlit.components.v1 as components

game_urls = {
    "getaway_shootout": "https://selenite.cc/semag/getawayshooter/index.html"
}


webpages = ["Home", "Games", "PictureOfTheDay"]
selected_page = st.sidebar.radio("Navigation", webpages)

#


if selected_page == webpages[0]:
    st.title("Chromium")
    st.write("Versatile web proxy. For my guys at school.")




    
    
if selected_page == webpages[1]:
    st.subheader("Getaway Shootout!")
    js_code = f"""
    <script>
        function openBlank() {{
            var win = window.open();
            var iframe = win.document.createElement("iframe");
            iframe.style.width = "100%";
            iframe.style.height = "100%";
            iframe.src = "{game_urls["getaway_shootout"]}";
            win.document.body.style.margin = "0";
            win.document.body.style.overflow = "hidden";
            win.document.body.appendChild(iframe);
        }}
    </script>
    <button onclick="openBlank()" style="font-size:20px;padding:10px;">Play in a Blank Tab</button>
    """

    st.markdown(js_code, unsafe_allow_html=True)


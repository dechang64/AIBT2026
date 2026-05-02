import streamlit.components.v1 as components

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=6000, scrolling=True)

import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Forum on AI & BioTech 2026")

# 隐藏 Streamlit 默认 UI
hide_css = """
<style>
    [data-testid="stToolbar"], [data-testid="stHeader"], [data-testid="stSidebar"],
    #MainMenu, footer { display: none !important; }
    .block-container { padding-top: 0; padding-bottom: 0; max-width: 100%; }
</style>
"""
st.markdown(hide_css, unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=6000, scrolling=True, use_container_width=True)

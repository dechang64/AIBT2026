import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(layout="wide", page_title="Forum on AI & BioTech 2026")

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

# Inject PDF base64 data into placeholders
pdf_dir = "pdfs"
for i in range(20):  # scan up to 20 PDFs
    pdf_path = os.path.join(pdf_dir, f"speaker_{i}.pdf")
    placeholder = f"__PDF_PLACEHOLDER_{i}__"
    if placeholder in html and os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pf:
            b64 = base64.b64encode(pf.read()).decode()
        html = html.replace(placeholder, f"data:application/pdf;base64,{b64}")

components.html(html, height=6000, scrolling=True, use_container_width=True)

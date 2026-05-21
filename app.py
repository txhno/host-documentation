from pathlib import Path
from base64 import b64encode

import streamlit as st
import streamlit.components.v1 as components


DOC_PATH = Path(__file__).with_name("copilot.html")
DOWNLOAD_PATH = Path(__file__).with_name(
    "rubick_ai_copilot_api_fresher_documentation.docx"
)


st.set_page_config(
    page_title="Rubick AI Copilot API Documentation",
    page_icon=":blue_book:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def build_download_pill() -> str:
    encoded_document = b64encode(DOWNLOAD_PATH.read_bytes()).decode("ascii")
    return (
        '<a class="pill" '
        f'href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{encoded_document}" '
        f'download="{DOWNLOAD_PATH.name}">Download DOCX</a>'
    )


def load_document() -> str:
    html = DOC_PATH.read_text(encoding="utf-8")
    if not DOWNLOAD_PATH.exists():
        return html

    old_metadata = """        <span class="pill">Last updated: <time datetime="2026-05-21">21 May 2026</time></span>
        <span class="pill">Self-contained HTML</span>
        <span class="pill">Images open in zoom view</span>"""
    new_metadata = f"""        <span class="pill">Last updated: <time datetime="2026-05-21">21 May 2026</time></span>
        {build_download_pill()}"""
    return html.replace(old_metadata, new_metadata)


if not DOC_PATH.exists():
    st.error("Missing copilot.html next to app.py.")
    st.stop()

st.markdown(
    """
    <style>
      .block-container {
        max-width: none;
        padding: 0;
      }
      header[data-testid="stHeader"],
      div[data-testid="stToolbar"],
      footer {
        display: none;
      }
      iframe {
        display: block;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

if not DOWNLOAD_PATH.exists():
    st.error(f"Missing {DOWNLOAD_PATH.name} next to app.py.")

components.html(load_document(), height=1200, scrolling=True)

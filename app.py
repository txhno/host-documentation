from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


DOC_PATH = Path(__file__).with_name("copilot.html")


st.set_page_config(
    page_title="Rubick AI Copilot API Documentation",
    page_icon=":blue_book:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def load_document() -> str:
    return DOC_PATH.read_text(encoding="utf-8")


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

components.html(load_document(), height=1200, scrolling=True)

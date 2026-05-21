from pathlib import Path

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
      .download-bar {
        position: sticky;
        top: 0;
        z-index: 1000;
        display: flex;
        justify-content: flex-end;
        gap: 12px;
        padding: 12px 20px;
        background: #ffffff;
        border-bottom: 1px solid #d8e1ee;
      }
      .stDownloadButton > button {
        border-radius: 8px;
        border: 1px solid #2457d6;
        background: #2457d6;
        color: #ffffff;
        font-weight: 700;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="download-bar">', unsafe_allow_html=True)
if DOWNLOAD_PATH.exists():
    st.download_button(
        "Download DOCX",
        data=DOWNLOAD_PATH.read_bytes(),
        file_name=DOWNLOAD_PATH.name,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
else:
    st.error(f"Missing {DOWNLOAD_PATH.name} next to app.py.")
st.markdown("</div>", unsafe_allow_html=True)

components.html(load_document(), height=1200, scrolling=True)

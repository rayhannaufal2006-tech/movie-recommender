import streamlit as st

def load_theme(dark_mode: bool):
    css = f"""
    <style>

    /* GLOBAL TRANSITION */
    * {{
        transition: 
            background-color 0.35s ease,
            color 0.35s ease,
            box-shadow 0.35s ease,
            border-color 0.35s ease,
            transform 0.25s ease;
    }}

    /* MAIN APP */
    [data-testid="stAppViewContainer"] {{
        background-color: {"#0b1220" if dark_mode else "#f5f7fb"};
        color: {"#f8fafc" if dark_mode else "#0f172a"};
    }}

    /* SIDEBAR */
    [data-testid="stSidebar"] {{
        background-color: {"#020617" if dark_mode else "#ffffff"};
    }}

    /* INPUT SEARCH */
    input {{
        background-color: {"#020617" if dark_mode else "#ffffff"} !important;
        color: {"white" if dark_mode else "black"} !important;
        border-radius: 16px !important;
        padding: 14px !important;
        font-size: 18px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(0,0,0,.15);
    }}

    /* SLIDER */
    .stSlider > div {{
        color: {"white" if dark_mode else "black"};
    }}

    /* MOVIE CARD */
    .movie-card {{
        background: {"#111827" if dark_mode else "#ffffff"};
        border-radius: 22px;
        padding: 14px;
        box-shadow: 0 20px 40px rgba(0,0,0,.25);
    }}

    .movie-card:hover {{
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 30px 60px rgba(0,0,0,.45);
    }}

    /* GENRE TAG */
    .genre-tag {{
        display:inline-block;
        padding:4px 12px;
        margin:4px 4px 0 0;
        border-radius:20px;
        font-size:12px;
        background:linear-gradient(135deg,#6366f1,#22d3ee);
        color:white;
    }}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

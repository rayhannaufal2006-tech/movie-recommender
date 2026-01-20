import streamlit as st
from data.movies import films, DEFAULT_POSTER
from ai.recommender import ai_recommend
from ui.theme import load_theme
from ui.components import render_movies

st.set_page_config(
    page_title="MovieFinder AI",
    page_icon="🎬",
    layout="wide"
)

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

if "user_genres" not in st.session_state:
    st.session_state.user_genres = []

_, col = st.columns([9, 1])
with col:
    st.session_state.dark_mode = st.toggle("🌗", st.session_state.dark_mode)

load_theme(st.session_state.dark_mode)

st.markdown(
    """
    <h1 style="text-align:center;">🎬 MovieFinder AI</h1>
    <p style="text-align:center; opacity:.7;">
    Cari film favoritmu dan biarkan AI merekomendasikan otomatis
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

search = st.text_input(
    "",
    placeholder="🔍 Cari film…",
    label_visibility="collapsed"
)

min_rating = st.slider("⭐ Minimal Rating", 1.0, 10.0, 7.0, 0.1)

recommended = ai_recommend(films, st.session_state.user_genres)

results = [
    f for f in recommended
    if search.lower() in f["judul"].lower()
    and f["rating"] >= min_rating
]

st.markdown(f"### 🎥 Ditemukan {len(results)} film")

render_movies(results, DEFAULT_POSTER)

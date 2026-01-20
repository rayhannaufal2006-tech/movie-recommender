import streamlit as st

def render_movies(results, default_poster):
    cols = st.columns(5)

    for i, film in enumerate(results):
        with cols[i % 5]:
            poster = film.get("poster", default_poster)
            st.image(poster, use_container_width=True)

            st.markdown('<div class="movie-card">', unsafe_allow_html=True)
            st.markdown(f"**{film['judul']}**")

            for g in film["genre"]:
                st.markdown(f"<span class='genre-tag'>{g}</span>", unsafe_allow_html=True)

            st.markdown(f"⭐ {film['rating']}")

            if st.button("❤️ Suka", key=film["judul"]):
                st.session_state.user_genres.extend(film["genre"])
                st.toast("AI mempelajari selera kamu 🤖")

            st.markdown("</div>", unsafe_allow_html=True)

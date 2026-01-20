from collections import Counter

def ai_recommend(films, user_genres):
    if not user_genres:
        return sorted(films, key=lambda x: x["rating"], reverse=True)

    fav = Counter(user_genres).most_common(1)[0][0]

    return sorted(
        [f for f in films if fav in f["genre"]],
        key=lambda x: x["rating"],
        reverse=True
    )

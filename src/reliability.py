from src.recommender import recommend_songs

# Reliability test to check consistency of recommendations across multiple runs.
def compute_overlap(list_a, list_b):
    """Measures how similar two recommendation lists are."""

    set_a = set(song[0]["title"] for song in list_a)
    set_b = set(song[0]["title"] for song in list_b)

    if len(set_a) == 0:
        return 0.0

    return len(set_a.intersection(set_b)) / len(set_a)

# Reliability test to check consistency of recommendations across multiple runs.
def test_reliability(profile, songs, runs=3, k=5):
    """Runs recommender multiple times and checks consistency."""

    results = []

    for _ in range(runs):
        recs = recommend_songs(profile["prefs"], songs, k=k)
        results.append(recs)

    overlaps = []

    for i in range(len(results) - 1):
        overlap = compute_overlap(results[i], results[i + 1])
        overlaps.append(overlap)

    avg_overlap = sum(overlaps) / len(overlaps)

    return {
        "profile": profile["name"],
        "stability_score": avg_overlap,
        "runs": runs
    }
"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs
from src.reliability import test_reliability

profiles = [
    {
        "name": "high_energy_conflicting_mood",
        "prefs": {"genre": "rock", "mood": "calm", "energy": 0.95},
    },
    {
        "name": "extreme_genre_mismatch",
        "prefs": {"genre": "classical", "mood": "happy", "energy": 0.7},
    },
    {
        "name": "low_energy_high_valence_mismatch",
        "prefs": {"genre": "jazz", "mood": "sad", "energy": 0.1},
    },
    {
        "name": "balanced_profile",
        "prefs": {"genre": "pop", "mood": "neutral", "energy": 0.5},
    },
]


def main() -> None:
    songs = load_songs("data/songs.csv")
    print("Loaded songs:", len(songs))

    # -------------------------
    # RECOMMENDATIONS PHASE
    # -------------------------
    for profile in profiles:
        print("\n=== " + profile["name"] + " ===\n")

        recommendations = recommend_songs(profile["prefs"], songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}\n")

    # -------------------------
    # RELIABILITY PHASE
    # -------------------------
    print("\n=== AI RELIABILITY EVALUATION PHASE ===\n")

    for profile in profiles:
        result = test_reliability(profile, songs, runs=3)

        print(f"{result['profile']}")
        print(f"Stability Score: {result['stability_score']:.2f}\n")


if __name__ == "__main__":
    main()

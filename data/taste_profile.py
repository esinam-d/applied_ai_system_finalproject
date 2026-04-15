user_profile= {
    """
    User taste profile dictionary for music recommendation simulation.

    This profile represents a user's musical preferences and targets for song recommendations.
    The profile emphasizes upbeat, energetic music with strong rhythmic and emotional qualities.

    Attributes:
        preferred_genre (str): Primary genre preference set to "afrobeats", indicating a preference
            for African rhythm-influenced music.
        preferred_mood (str): Desired emotional tone set to "happy", targeting positive and uplifting songs.
        target_energy (float): Energy level target of 0.75 (on a 0-1 scale), representing moderately
            high-energy music preferences.
        target_tempo (int): Preferred beats per minute set to 100 BPM, indicating uptempo music.
        target_danceability (float): Danceability target of 0.8 (on a 0-1 scale), emphasizing music
            with strong rhythmic elements suitable for dancing.
        target_valence (float): Musical positivity target of 0.7 (on a 0-1 scale), reflecting preference
            for upbeat and cheerful musical characteristics.

    Analysis:
        This profile is MODERATELY WEIGHTED toward high-energy music but has LIMITED DISTINCTION
        between high-energy and relaxed genres. The tight clustering of high values (energy: 0.75,
        danceability: 0.8, valence: 0.7) strongly favors upbeat music and would effectively exclude
        low-fi and relaxed genres. However, the profile lacks explicit anti-preferences or negative
        parameters for relaxed characteristics, making it somewhat one-dimensional. For better
        distinction between contrasting genres, consider adding constraints for minimum energy/tempo
        thresholds or separate "chill mode" profiles with lower targets.
    """
    "preferred_genre": "afrobeats"
    "preferred_mood": "happy",
    "target_energy": 0.75,
    "target_tempo": 100,
    "target_danceability": 0.8,
    "target_valence": 0.7
}

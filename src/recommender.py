import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # Convert UserProfile to dict format for scoring
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }
        
        scored_songs = []
        for song in self.songs:
            # Convert Song dataclass to dict for scoring
            song_dict = {
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
            }
            score, reasons = score_song(user_prefs, song_dict)
            scored_songs.append((song, score, reasons))
        
        # Sort by score (descending) and return top k
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        return [song for song, score, reasons in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # Convert UserProfile to dict format for scoring
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }
        
        # Convert Song to dict for scoring
        song_dict = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
        }
        
        score, reasons = score_song(user_prefs, song_dict)
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric fields to floats
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a similarity score and explanation for a song given user preferences."""
    score = 0.0
    reasons = []

    # Genre match
    if user_prefs["genre"] == song["genre"]:
        score += 1.0
        reasons.append("genre match (+1.0)")

    # Mood match
    if user_prefs["mood"] == song["mood"]:
        score += 1.5
        reasons.append("mood match (+1.5)")

    # Energy similarity
    energy_score = max(0, 1 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_score * 2

    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    return score, reasons


"""Rank songs by score and return the top k recommendations with explanations."""
def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)

        # Create a simple explanation from the reasons
        explanation = ", ".join(reasons)

        scored_songs.append((song, score, explanation))
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    return scored_songs[:k]

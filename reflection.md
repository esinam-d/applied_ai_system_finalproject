## Reflection: Profile Comparisons

I tested four user profiles: high-energy conflicting mood, extreme genre mismatch, low-energy high-valence mismatch, and a balanced profile.

- High-energy vs Low-energy profile:  
The high-energy profile ranked songs like "Gym Hero" and "Sunrise City" at the top because they match the high energy preference. The low-energy profile instead favored calmer songs like "Rooftop Lights" and "Midnight Bloom." This makes sense because energy similarity strongly affects the scoring system.

- Genre-focused vs Genre-mismatch profile:  
The genre-focused profile consistently pushed pop songs higher, while the genre-mismatch profile still often returned similar results because the dataset is small and mostly contains pop and closely related genres. This shows that dataset imbalance affects how much genre actually influences diversity.

- Conflicting vs Balanced profile:  
The conflicting profile (high energy but calm mood) produced mixed results, with songs scoring well in one feature but poorly in another. The balanced profile produced more stable rankings with no single feature dominating too strongly. This makes sense because balanced inputs reduce extreme weighting effects in the scoring system.

Overall, the differences between profiles show that the recommender is very sensitive to energy and moderately sensitive to genre and mood, which matches how the scoring function is designed.
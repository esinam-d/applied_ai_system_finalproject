# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
Ans.) SongPulse Engine

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

Ans.) This recommender is designed to suggest songs that match a user’s musical “vibe” based on features like mood, genre, and energy.

It assumes that user taste can be represented using simple numeric and categorical preferences. It also assumes that similarity between songs can be measured using weighted scoring of features.

This system is for classroom learning and experimentation, not for real-world music recommendations.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.
Ans.) The model uses song features like genre, mood, energy, tempo, valence, and danceability to determine how well a song matches a user’s preferences.

Each user has preferences such as favorite genre, mood, and target energy level. The system compares each song to these preferences and assigns points based on how closely they match.

Exact matches like genre and mood give fixed bonus points, while numerical features like energy are scored based on how close they are to the target value.

The final score is a weighted combination of all features, and songs are ranked from highest to lowest score. Compared to the starter version, I improved the system by making energy similarity more structured and combining multiple features into one scoring system.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  
Ans.) The dataset contains 18 songs stored in a CSV file.

The songs include a mix of genres like pop, rock, jazz, and electronic, with different moods such as happy, calm, and energetic.

Each song has numeric features like energy, tempo, valence, danceability, and acousticness.

The dataset is small and limited, so some genres and moods are underrepresented, which affects recommendation diversity.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  
Ans.) The system works well for users with clear preferences, such as high-energy pop or calm acoustic listeners.

It captures patterns between energy level and mood reasonably well, which helps create believable recommendations.

In many cases, the top recommended songs match the expected “vibe” of the user profile, especially when preferences are not conflicting.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  
Ans.) One weakness I discovered is that the recommender system over-relies on exact genre and mood matches. This creates a filter bubble where songs from the same genre and mood are repeatedly recommended, even when other songs might have a similar overall vibe. I also noticed that the small dataset limits diversity, which makes it harder for the system to provide varied recommendations for different user preferences. As a result, the system tends to favor a narrow range of songs instead of exploring broader musical options.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.
Ans.) I tested the recommender system using four different user profiles: a high-energy conflicting mood profile, an extreme genre mismatch profile, a low-energy high-valence profile, and a balanced profile.

I looked at whether the top recommended songs matched the general “vibe” of each profile, especially focusing on how energy, mood, and genre influenced the rankings. I expected high-energy profiles to prioritize fast and intense songs, and low-energy profiles to favor calmer tracks.

What surprised me was how strongly small changes in energy values affected the final ranking. Even when genre stayed the same, songs would move up or down significantly based on energy similarity. I also noticed that profiles with unusual or conflicting preferences sometimes still produced similar results because the dataset is small and limited in variety.

Overall, the system behaved as expected, but it is very sensitive to energy and does not handle conflicting preferences in a nuanced way.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  
Ans.) If I continued improving this system, I would add more songs and a wider variety of genres and moods to improve diversity.

I would also improve the scoring system to better handle conflicting preferences by balancing features instead of treating them independently.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Ans.) This project helped me understand how recommender systems convert user preferences into ranked results using simple scoring rules.

I learned that even small changes in weights or feature values can significantly change the recommendations.

One interesting insight was that these systems do not actually “understand” music, but instead calculate similarity using data features.

Using AI tools like Copilot and ChatGPT, helped me design and debug faster, but I still had to check that the logic made sense.

Overall, I now see how real recommendation systems are built from simple components that are carefully tuned to produce good results.

If I extended this project, I would add a diversity rule so the system does not return songs that are too similar to each other.
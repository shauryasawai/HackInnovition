texts = [
    "I am very happy today", "I feel so sad and depressed", "This is the best day ever", "I am so angry and frustrated",
    "I am feeling excited about the new project", "I am worried about the results", "I am grateful for my family",
    "I feel lonely and isolated", "I am feeling content with my achievements", "I am scared of the dark",
    "I am feeling joyful", "I feel so disappointed", "This is an amazing experience", "I am furious with the service",
    "I am enthusiastic about the new course", "I am anxious about the interview", "I am feeling blessed",
    "I feel abandoned and alone", "I am proud of my work", "I am terrified of heights", "I am delighted with the surprise",
    "I feel miserable and down", "I am ecstatic about the promotion", "I am feeling bitter about the situation",
    "I am thrilled to see you", "I feel hopeless and lost", "I am on cloud nine", "I am fuming with rage",
    "I am energized by the workout", "I feel heartbroken", "I am jubilant with our victory", "I am irritated by the delay",
    "I am hopeful for the future", "I feel rejected and unwanted", "I am pleased with the outcome", "I am nervous about the presentation",
    "I feel secure and safe", "I am feeling melancholic today", "I am satisfied with the service", "I am distressed by the news",
    "I feel refreshed after the vacation", "I am resentful of their success", "I am optimistic about the project",
    "I feel dejected", "I am amused by the joke", "I am uneasy about the test", "I feel comforted by your words",
    "I am relaxed and calm", "I am unsettled by the changes", "I feel uplifted by the music", "I am in awe of the beauty",
    "I feel stressed about the deadline", "I am grateful for the opportunity", "I am feeling peaceful", "I feel suffocated by the rules",
    "I am inspired by the story", "I feel uneasy in crowded places", "I am thankful for your help", "I am disheartened by the loss",
    "I am ecstatic about the trip", "I feel anxious and worried", "I am delighted to meet you", "I am feeling optimistic today"
]
moods = [
    "happy", "sad", "happy", "angry", "excited", "worried", "grateful", "lonely", "content", "scared",
    "happy", "sad", "happy", "angry", "excited", "anxious", "grateful", "lonely", "proud", "scared", 
    "happy", "sad", "happy", "angry", "happy", "sad", "happy", "angry", "excited", "sad", 
    "happy", "angry", "hopeful", "sad", "content", "anxious", "safe", "sad", "content", "sad", 
    "happy", "angry", "hopeful", "sad", "happy", "anxious", "content", "calm", "anxious", "happy", 
    "awe", "stressed", "grateful", "calm", "suffocated", "inspired", "anxious", "grateful", "sad", 
    "happy", "anxious", "happy", "hopeful"
]
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Convert texts to a matrix of token counts
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X, moods)

# Save the model and vectorizer
joblib.dump(model, 'mood_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

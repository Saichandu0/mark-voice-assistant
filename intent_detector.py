from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import re
from training_data import training_sentences, training_labels
import nltk_init  # This will handle NLTK initialization silently

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

class IntentDetector:
    def __init__(self):
        # Preprocess training sentences
        self.processed_sentences = [preprocess_text(sentence) for sentence in training_sentences]
        
        # Initialize and train the classifier
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        X = self.vectorizer.fit_transform(self.processed_sentences)
        self.classifier = LogisticRegression(max_iter=1000)
        self.classifier.fit(X, training_labels)
        
        # Define location phrases for fallback detection
        self.location_phrases = [
            "restaurant", "eat", "hungry", "starving", "food", "cafe", "coffee",
            "hotel", "stay", "mall", "shop", "park", "visit", "gym", "workout",
            "nearby", "near me", "around here", "place", "find", "suggest",
            "bar", "drink", "store", "buy", "accommodation", "where can i",
            "looking for", "need a place", "want to", "find me", "location",
            "where am i", "my location", "current location", "where is",
            "where are we", "where is this", "what is my location",
            "tell me my location", "show me my location", "find my location",
            "locate me", "where is this place", "what's my location",
            "where are we now", "where is this", "where is here"
        ]
        
        # Define time-related phrases for better detection
        self.time_phrases = [
            "time", "what time", "current time", "tell me the time",
            "what's the time", "time is it", "time now", "time currently",
            "what time is it now", "current time", "time please"
        ]
        
        # Define capability-related phrases
        self.capability_phrases = [
            "what can you", "what are your", "tell me what you", "what do you",
            "capabilities", "features", "functions", "abilities", "help with",
            "capable of", "can you do", "what are your skills", "what can you tell",
            "what can you show", "what can you teach", "what can you help"
        ]

        # Define music-related phrases
        self.music_phrases = [
            "play music", "play a song", "play some music", "start the music",
            "play a tune", "play youtube", "play on youtube", "show me music",
            "show me songs", "best music", "best songs", "play something",
            "play something good", "play something nice", "play something cool",
            "play a track", "play a beat", "play some tunes", "play some beats",
            "play some tracks", "play some songs", "play some good music"
        ]

        # Define weather-related phrases
        self.weather_phrases = [
            "weather", "forecast", "rain", "sunny", "cloudy", "temperature",
            "how's the weather", "what's the weather", "weather update",
            "weather forecast", "is it going to rain", "will it rain"
        ]

        # Define web search phrases
        self.web_search_phrases = [
            "search", "google", "look up", "find", "information about",
            "search for", "search the web", "look up on google", "search online",
            "find on google", "search something", "google this"
        ]

        # Define general knowledge phrases
        self.general_knowledge_phrases = [
            "who is", "what is", "tell me about", "who was", "what are",
            "who are", "information about", "details about", "facts about",
            "who are the", "tell me more about", "what do you know about",
            "can you tell me about", "what can you tell me about", "what's the story about"
        ]

    def detect_intent(self, text):
        # Preprocess the input text
        processed_text = preprocess_text(text)
        X_test = self.vectorizer.transform([processed_text])
        prediction = self.classifier.predict(X_test)[0]
        
        # Get prediction probabilities
        probabilities = self.classifier.predict_proba(X_test)[0]
        max_probability = max(probabilities)
        
        # If the highest probability is too low, check for specific phrases
        if max_probability < 0.4:  # Lower threshold for better generalization
            # Check for location-based phrases first (moved to top priority)
            if any(phrase in processed_text for phrase in self.location_phrases):
                return "location_query"
            # Check for music-related phrases
            elif any(phrase in processed_text for phrase in self.music_phrases):
                return "play_music"
            # Check for weather-related phrases
            elif any(phrase in processed_text for phrase in self.weather_phrases):
                return "weather_query"
            # Check for web search phrases
            elif any(phrase in processed_text for phrase in self.web_search_phrases):
                return "web_search"
            # Check for time-related phrases
            elif any(phrase in processed_text for phrase in self.time_phrases):
                return "get_time"
            # Check for general knowledge phrases
            elif any(phrase in processed_text for phrase in self.general_knowledge_phrases):
                return "general_knowledge"
            # Check for capability-related phrases
            elif any(phrase in processed_text for phrase in self.capability_phrases):
                return "capability_query"
            return "fallback"
        return prediction 
import speech_recognition as sr
import pyttsx3
import webbrowser
from intent_detector import IntentDetector

# Initialize the intent detector
intent_detector = IntentDetector()

# Text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I did not get you")
            return None
        except sr.RequestError:
            speak("Sorry, I did not get you")
            return None

# Perform action based on intent
def handle_intent(intent, query):
    try:
        if intent == "weather_query":
            speak("Got it")
            speak("Opening weather forecast.")
            webbrowser.open("https://www.google.com/search?q=weather")
        elif intent == "web_search":
            speak("Got it")
            speak("Searching that on Google.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif intent == "play_music":
            speak("Got it")
            speak("Playing some music on YouTube.")
            webbrowser.open("https://www.youtube.com/results?search_query=lofi+beats")
        elif intent == "get_time":
            speak("Got it")
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
        elif intent == "general_knowledge":
            speak("Got it")
            speak("Let me search that for you.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif intent == "location_query":
            speak("Got it")
            speak("Let me help you find that.")
            # Add "near me" to the search query for better local results
            search_query = f"{query} near me"
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif intent == "personal_question":
            speak("I'm just a simple AI assistant, so I don't have personal feelings or opinions. I'm here to help you with tasks like checking the weather, searching the web, playing music, or telling the time.")
        elif intent == "greeting":
            speak("Hello! I'm Mike, your AI assistant. I can help you with checking the weather, searching the web, playing music, telling the time, finding places, or looking up information about people and things.")
        elif intent == "fallback":
            # Check for location-based queries in fallback
            location_phrases = ["find me", "suggest", "where can I", "I'm hungry", "I need", "looking for"]
            if any(phrase in query.lower() for phrase in location_phrases):
                speak("Let me help you find that.")
                search_query = f"{query} near me"
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            # Check for personal questions in fallback
            elif any(phrase in query.lower() for phrase in ["about me", "do you like me", "think about me", "feel about me", "opinion about me"]):
                speak("I'm just a simple AI assistant, so I don't have personal feelings or opinions. I'm here to help you with tasks like checking the weather, searching the web, playing music, or telling the time.")
            # Check for general knowledge questions in fallback
            elif any(phrase in query.lower() for phrase in ["who is", "what is", "tell me about", "who was"]):
                speak("Let me search that for you.")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("I'm not sure I understand that request. I can help you with weather, web searches, playing music, telling the time, finding places, or looking up information about people and things.")
        else:
            speak("I am unable to do the requested task as of the moment")
    except Exception as e:
        speak("I am unable to do the requested task as of the moment")

# Run the assistant
def run_mini_assistant():
    text = listen()
    if text is None:  # If speech recognition failed
        return
    if text:
        # Check if the input starts with "hey mike"
        if text.lower().startswith("hey mike"):
            # Remove "hey mike" from the input for intent detection
            query = text[8:].strip()
            if query:  # Only proceed if there's a query after "hey mike"
                intent = intent_detector.detect_intent(query)
                print(f"Detected intent: {intent}")
                handle_intent(intent, query)
            else:
                speak("I am unable to do the requested task as of the moment")

if __name__ == "__main__":
    run_mini_assistant()


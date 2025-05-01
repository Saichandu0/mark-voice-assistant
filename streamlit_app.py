import streamlit as st
import speech_recognition as sr
import pyttsx3
import webbrowser
from intent_detector import IntentDetector
from datetime import datetime
import time

# Initialize the intent detector
intent_detector = IntentDetector()

# Initialize text-to-speech engine
engine = None

# Text-to-speech
def speak(text):
    global engine
    try:
        if engine is None:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # Speed of speech
            engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
        
        # Stop any ongoing speech
        engine.stop()
        
        # Start new speech
        engine.say(text)
        engine.runAndWait()
        
        # Reset engine after speaking
        engine = None
    except Exception as e:
        st.warning(f"Could not speak: {str(e)}")
        # Reset engine on error
        engine = None

# Speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Add listening class to app and button
        st.markdown("""
            <script>
                setTimeout(function() {
                    document.querySelector('.stApp').classList.add('listening');
                    document.querySelector('.stButton>button').classList.add('listening');
                }, 100);
            </script>
        """, unsafe_allow_html=True)
        
        # Show listening animation
        with st.spinner("🎤 Listening..."):
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                st.success(f"🎯 You said: {text}")
                
                # Remove listening class from app and button
                st.markdown("""
                    <script>
                        setTimeout(function() {
                            document.querySelector('.stApp').classList.remove('listening');
                            document.querySelector('.stButton>button').classList.remove('listening');
                        }, 100);
                    </script>
                """, unsafe_allow_html=True)
                
                # Common name corrections
                name_corrections = {
                    "el": "elon musk",
                    "elon": "elon musk",
                    "musk": "elon musk",
                    "steve": "steve jobs",
                    "jobs": "steve jobs",
                    "bill": "bill gates",
                    "gates": "bill gates",
                    "mark": "mark zuckerberg",
                    "zuckerberg": "mark zuckerberg",
                    "jeff": "jeff bezos",
                    "bezos": "jeff bezos",
                    "tim": "tim cook",
                    "cook": "tim cook",
                    "sundar": "sundar pichai",
                    "pichai": "sundar pichai"
                }
                
                # Apply name corrections only after the wake word
                words = text.lower().split()
                corrected_words = []
                
                # Check if the text starts with "hey mark"
                if len(words) >= 2 and words[0] == "hey" and words[1] == "mark":
                    # Keep "hey mark" as is
                    corrected_words.extend(words[:2])
                    # Apply corrections to the rest of the words
                    for word in words[2:]:
                        if word in name_corrections:
                            corrected_words.append(name_corrections[word])
                        else:
                            corrected_words.append(word)
                else:
                    # Apply corrections to all words if not starting with "hey mark"
                    for word in words:
                        if word in name_corrections:
                            corrected_words.append(name_corrections[word])
                        else:
                            corrected_words.append(word)
                
                corrected_text = ' '.join(corrected_words)
                if corrected_text != text.lower():
                    st.info(f"🎯 Corrected to: {corrected_text}")
                return corrected_text
            except sr.UnknownValueError:
                st.error("❌ Sorry, I did not get you")
                # Remove listening class from app and button
                st.markdown("""
                    <script>
                        setTimeout(function() {
                            document.querySelector('.stApp').classList.remove('listening');
                            document.querySelector('.stButton>button').classList.remove('listening');
                        }, 100);
                    </script>
                """, unsafe_allow_html=True)
                return None
            except sr.RequestError:
                st.error("❌ Sorry, I did not get you")
                # Remove listening class from app and button
                st.markdown("""
                    <script>
                        setTimeout(function() {
                            document.querySelector('.stApp').classList.remove('listening');
                            document.querySelector('.stButton>button').classList.remove('listening');
                        }, 100);
                    </script>
                """, unsafe_allow_html=True)
                return None

# Perform action based on intent
def handle_intent(intent, query):
    try:
        if intent == "weather_query":
            response = "Opening weather forecast for you."
            st.info("🌤️ " + response)
            speak(response)
            webbrowser.open("https://www.google.com/search?q=weather")
        elif intent == "web_search":
            response = f"Searching for {query} on Google."
            st.info("🔍 " + response)
            speak(response)
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif intent == "play_music":
            response = "Playing some relaxing music on YouTube."
            st.info("🎵 " + response)
            speak(response)
            webbrowser.open("https://www.youtube.com/results?search_query=lofi+beats")
        elif intent == "get_time":
            current_time = datetime.now().strftime("%H:%M")
            response = f"The current time is {current_time}"
            st.info("⏰ " + response)
            speak(response)
        elif intent == "general_knowledge":
            response = f"Let me search for information about {query}"
            st.info("📚 " + response)
            speak(response)
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif intent == "location_query":
            response = f"Let me help you find {query} near you"
            st.info("📍 " + response)
            speak(response)
            search_query = f"{query} near me"
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif intent == "personal_question":
            response = "I'm just a simple AI assistant, so I don't have personal feelings or opinions. I'm here to help you with tasks like checking the weather, searching the web, playing music, or telling the time."
            st.info("🤖 " + response)
            speak(response)
        elif intent == "greeting":
            current_time = datetime.now().hour
            greeting = "Good morning" if 5 <= current_time < 12 else "Good afternoon" if 12 <= current_time < 18 else "Good evening"
            
            response = f"""{greeting}! I'm Mark, your AI assistant. Here's what I can do for you:

1. Check the weather and forecast 🌤️
2. Search the web for any information 🔍
3. Play relaxing music on YouTube 🎵
4. Tell you the current time ⏰
5. Find places near you (restaurants, cafes, etc.) 📍
6. Look up information about people and things 📚
7. Answer general knowledge questions

Just say "Hey Mark" followed by what you'd like me to do!"""
            
            st.info("👋 " + response)
            speak(f"{greeting}! I'm Mark, your AI assistant. I can help you with checking the weather, searching the web, playing music, telling the time, finding places, or looking up information. Just say 'Hey Mark' followed by what you'd like me to do!")
        elif intent == "capability_query":
            response = """I can help you with many things! Here's what I can do:
1. Tell you the current time ⏰
2. Check the weather for you 🌤️
3. Search the web for information 🔍
4. Play music on YouTube 🎵
5. Find places near you (restaurants, cafes, hotels, etc.) 📍
6. Look up information about people and things 📚
7. Answer general knowledge questions
Just start your request with 'Hey Mark' and I'll help you out!"""
            st.info("💡 " + response)
            speak("I can help you with many things! I can tell you the time, check the weather, search the web, play music, find places near you, and look up information about people and things. Just start your request with 'Hey Mark' and I'll help you out!")
        elif intent == "fallback":
            response = "I'm not sure I understand that request. I can help you with weather, web searches, playing music, telling the time, finding places, or looking up information about people and things."
            st.info("🤔 " + response)
            speak(response)
        else:
            response = "I am unable to do the requested task as of the moment"
            st.error("❌ " + response)
            speak(response)
    except Exception as e:
        response = "I am unable to do the requested task as of the moment"
        st.error("❌ " + response)
        speak(response)

# Main Streamlit app
def main():
    # Set page config
    st.set_page_config(
        page_title="Mark - Voice Assistant",
        page_icon="🎤",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Main container
    with st.container():
        # Header
        st.markdown("""
            <div style='text-align: center; margin-bottom: 1rem;'>
                <h1>Mark</h1>
                <p style='color: #4fc3f7; font-size: 1.2em; margin-top: -1.5rem;'>Your Personal Mini Assistant</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Create a container for the button and messages
        button_container = st.empty()
        message_container = st.empty()
        
        with button_container.container():
            if st.button("", key="listen_button"):
                # Add listening class to app and button
                st.markdown("""
                    <style>
                        .stApp {
                            border: 12px solid #ff3b3b !important;
                            box-shadow: 0 0 30px rgba(255,59,59,0.5) !important;
                            animation: listeningGlow 1.5s infinite !important;
                        }
                        
                        .stButton>button {
                            border: 2px solid #ff3b3b !important;
                            box-shadow: 0 0 40px rgba(255,59,59,0.8) !important;
                            animation: listeningButtonGlow 1.5s infinite !important;
                        }
                        
                        @keyframes listeningGlow {
                            0% { box-shadow: 0 0 30px rgba(255,59,59,0.5); }
                            50% { box-shadow: 0 0 50px rgba(255,59,59,0.8); }
                            100% { box-shadow: 0 0 30px rgba(255,59,59,0.5); }
                        }
                        
                        @keyframes listeningButtonGlow {
                            0% { box-shadow: 0 0 40px rgba(255,59,59,0.8); }
                            50% { box-shadow: 0 0 60px rgba(255,59,59,1); }
                            100% { box-shadow: 0 0 40px rgba(255,59,59,0.8); }
                        }
                    </style>
                """, unsafe_allow_html=True)
                
                # Add a small delay for better UX
                time.sleep(0.5)
                text = listen()
                
                if text:
                    with message_container.container():
                        st.success(f"🎤 You said: {text}")
                        
                        # Check if the input starts with "hey mark"
                        if text.lower().startswith("hey mark"):
                            # Remove "hey mark" from the input for intent detection
                            query = text[8:].strip()
                            if query:  # If there's a query after "hey mark"
                                intent = intent_detector.detect_intent(query)
                                st.info(f"🎯 Detected intent: {intent}")
                                handle_intent(intent, query)
                            else:  # If only "hey mark" was said
                                handle_intent("greeting", "")
                        else:
                            st.warning("⚠️ Please start your request with 'Hey Mark'")
                    
                    # Remove listening styles after processing
                    st.markdown("""
                        <style>
                            .stApp {
                                border: 12px solid #1a1a1a !important;
                                box-shadow: 0 0 50px rgba(0,0,0,0.8) !important;
                                animation: none !important;
                            }
                            
                            .stButton>button {
                                border: none !important;
                                box-shadow: 0 0 30px rgba(79,195,247,0.6) !important;
                                animation: none !important;
                            }
                        </style>
                    """, unsafe_allow_html=True)
                    
                    # Add a delay before allowing the next button press
                    time.sleep(3)  # Wait for 3 seconds
                    
                    # Force a rerun to update the display
                    st.rerun()

    # Add custom CSS for iPhone-like interface
    st.markdown("""
        <style>
        /* Main container styling */
        .stApp {
            background-color: #000000;
            width: 450px;
            height: 975px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0.95);
            border-radius: 44px;
            overflow: hidden;
            box-shadow: 0 0 50px rgba(0,0,0,0.8);
            padding: 0;
            border: 12px solid #1a1a1a;
            transition: all 0.3s ease;
        }
        
        .stApp.listening {
            border-color: #ff3b3b;
            box-shadow: 0 0 30px rgba(255,59,59,0.5);
            animation: listeningGlow 1.5s infinite;
        }
        
        @keyframes listeningGlow {
            0% {
                border-color: #ff3b3b;
                box-shadow: 0 0 30px rgba(255,59,59,0.5);
            }
            50% {
                border-color: #ff3b3b;
                box-shadow: 0 0 50px rgba(255,59,59,0.8);
            }
            100% {
                border-color: #ff3b3b;
                box-shadow: 0 0 30px rgba(255,59,59,0.5);
            }
        }
        
        /* Ensure the body takes full height and centers content */
        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        
        /* Main content wrapper */
        .main .block-container {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Ensure the app takes full height and centers content */
        #root > div:first-child {
            height: 100vh;
            width: 100vw;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        
        /* Rest of your existing styles... */
        .stApp:hover {
            transform: translate(-50%, -50%) scale(0.96);
        }
        
        /* iPhone notch */
        .stApp::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 160px;  /* Slightly wider for iPhone 15 Pro */
            height: 35px;
            background-color: #000000;
            border-radius: 0 0 20px 20px;
            z-index: 1000;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }
        
        /* Dynamic Island */
        .stApp::after {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 130px;  /* Slightly wider for iPhone 15 Pro */
            height: 35px;
            background-color: #000000;
            border-radius: 20px;
            z-index: 1001;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }
        
        /* Main content area */
        .main .block-container {
            padding: 2.2rem 1.2rem;  /* Slightly more padding for larger screen */
            margin-top: 50px;
            max-width: 100%;
            background: linear-gradient(180deg, #000000 0%, #1a1a1a 100%);
        }
        
        /* Button styling */
        .stButton>button {
            width: 170px;
            height: 170px;
            border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, #4fc3f7, #0288d1);
            color: white;
            font-size: 1.2em;
            border: none;
            box-shadow: 0 0 30px rgba(79,195,247,0.6),
                        inset 0 0 20px rgba(255,255,255,0.2);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            margin: 3rem auto;
            display: block;
        }
        
        .stButton>button.listening {
            transform: scale(0.95);
            border: 2px solid #ff3b3b;
            animation: listeningButtonGlow 1.5s infinite;
        }
        
        @keyframes listeningButtonGlow {
            0% {
                box-shadow: 0 0 40px rgba(255,59,59,0.8),
                           inset 0 0 30px rgba(255,255,255,0.3);
                border-color: #ff3b3b;
            }
            50% {
                box-shadow: 0 0 60px rgba(255,59,59,1),
                           inset 0 0 40px rgba(255,255,255,0.4);
                border-color: #ff3b3b;
            }
            100% {
                box-shadow: 0 0 40px rgba(255,59,59,0.8),
                           inset 0 0 30px rgba(255,255,255,0.3);
                border-color: #ff3b3b;
            }
        }
        
        .stButton>button:hover {
            transform: scale(1.05) rotate(5deg);
            box-shadow: 0 0 40px rgba(79,195,247,0.8),
                       inset 0 0 30px rgba(255,255,255,0.3);
        }
        
        .stButton>button::before {
            content: '👤';
            font-size: 3em;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        
        .stButton>button::after {
            content: 'Start';
            position: absolute;
            bottom: 25px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.9em;
            color: white;
            text-shadow: 0 0 5px rgba(255,255,255,0.5);
        }
        
        /* Message styling */
        .stSuccess, .stError, .stInfo, .stWarning {
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            padding: 1rem;
            margin: 0.5rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            animation: fadeIn 0.3s ease;
            max-width: 90%;
            margin-left: auto;
            margin-right: auto;
            opacity: 1 !important;
            display: block !important;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .stSuccess {
            color: #28a745;
            border-left: 4px solid #28a745;
        }
        
        .stError {
            color: #dc3545;
            border-left: 4px solid #dc3545;
        }
        
        .stInfo {
            color: #17a2b8;
            border-left: 4px solid #17a2b8;
        }
        
        /* Title styling */
        h1 {
            color: #ffffff;
            text-align: center;
            font-size: 2em;
            margin-bottom: 2.5rem;
            margin-top: 2.5rem;
            text-shadow: 0 0 10px rgba(255,255,255,0.3);
            font-weight: 600;
            letter-spacing: 1px;
        }
        
        /* Hide scrollbar */
        ::-webkit-scrollbar {
            display: none;
        }
        
        /* Center content */
        .element-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        /* Status bar */
        .status-bar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 44px;
            background-color: rgba(0,0,0,0.8);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
            z-index: 1002;
        }
        
        .status-bar::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, 
                rgba(255,255,255,0) 0%,
                rgba(255,255,255,0.2) 50%,
                rgba(255,255,255,0) 100%);
        }
        
        .status-bar-time {
            color: white;
            font-size: 0.9em;
            font-weight: 600;
        }
        
        .status-bar-icons {
            display: flex;
            gap: 5px;
        }
        
        .status-bar-icon {
            color: white;
            font-size: 0.9em;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
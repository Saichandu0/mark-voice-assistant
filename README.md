Voice-Based Intent Detection Assistant (MARK) – Project Description

Overview: This project is a basic voice assistant that listens to user speech, understands the intent behind what they say using Natural Language Processing (NLP) techniques, and then performs a relevant action like opening a web search, telling the time, or playing music — similar to a mini version of Siri.

Key Features:

Speech Recognition: Uses a microphone to capture what the user says and convert it to text.

Intent Detection: Applies a machine learning model (Logistic Regression) trained on sample phrases to detect the user's intent.

Action Handling: Based on the detected intent, it can:

Search on Google

Play music on YouTube

Show weather information

Announce the current time

Text-to-Speech: Responds to the user by speaking using your system's voice engine.

How It Works:

Voice Input: The user speaks a sentence into the microphone (e.g., “play some music”).

Transcription: The sentence is converted to text using Google's Speech Recognition API.

Intent Detection:

The sentence is transformed into numeric form using TF-IDF vectorization.

A Logistic Regression classifier, trained on example commands, predicts the most likely intent (e.g., play_music).

Perform Action: The assistant carries out the corresponding action (e.g., opens YouTube with a music search).

Response: The assistant gives spoken feedback to the user (e.g., “Playing some music on YouTube”).

Technologies Used:

Python: Main programming language.

speech_recognition: For capturing and converting audio to text.

pyttsx3: For converting responses into speech.

NLTK: (Optional) for basic NLP support.

scikit-learn: For training and using the machine learning model.

TF-IDF Vectorizer: Converts text to numerical form.

Logistic Regression: Classifies user input into predefined intents.

webbrowser: Executes browser-based actions like Google search or YouTube.

Intent-detection-system-Mark-

Project Outcome: This assistant showcases how speech, NLP, and automation can work together to build an interactive and intelligent voice-controlled system using minimal resources. It provides a hands-on foundation to explore more advanced assistants using AI models like GPT or local LLMs.

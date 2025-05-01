# Training sentences for intent detection
training_sentences = [
    # Weather queries (8)
    "what's the weather like", "tell me the weather", "weather forecast", "how's the weather today",
    "what's the weather forecast", "is it going to rain", "will it rain today", "weather update",
    # Web search queries (10)
    "open Google", "search something", "google this", "search for", "look up",
    "find information about", "search the web for", "look up on google", "search online for", "find on google",
    # Music queries (15)
    "play a song", "play some music", "start the music", "play music", "play a tune",
    "play youtube", "play on youtube", "show me music", "show me songs", "best music",
    "best songs", "play something", "play something good", "play something nice", "play something cool",
    # Time queries (8)
    "what time is it", "tell me the time", "current time please", "what's the time",
    "what's the current time", "time now", "what time is it now", "current time",
    # General knowledge queries (15)
    "who is", "what is", "tell me about", "who was", "what are", "who are",
    "information about", "details about", "facts about", "who are the",
    "tell me more about", "what do you know about", "can you tell me about", "what can you tell me about", "what's the story about",
    # Location-based queries (25)
    "find me a restaurant", "suggest a good place to eat", "where can I eat", "I'm hungry",
    "find me a cafe", "suggest a coffee shop", "where can I get coffee",
    "find me a hotel", "suggest a place to stay", "where can I stay",
    "find me a mall", "suggest a shopping place", "where can I shop",
    "find me a park", "suggest a place to visit", "where can I go",
    "find me a gym", "suggest a fitness center", "where can I workout",
    "find me a bar", "suggest a place to drink", "where can I get a drink",
    "find me a store", "suggest a place to buy", "where can I buy",
    # Additional location-based variations (12)
    "I'm starving suggest me a good restaurant nearby", "I'm hungry find me a place to eat",
    "suggest me a good restaurant nearby", "find me a good place to eat nearby",
    "where can I find a good restaurant", "I need to eat something",
    "looking for a place to eat", "want to eat something",
    "find me something to eat", "where can I get food",
    "I need a place to stay", "where can I find accommodation",
    # Personal questions (8)
    "what do you think about me", "do you like me", "what do you like about me",
    "how do you feel about me", "what's your opinion about me",
    "what do you think of me", "do you like me as a person", "what's your view about me",
    # Greetings and basic interactions (60)
    "hello", "hi", "how are you", "good morning", "good afternoon", "good evening",
    "hey there", "hi there", "hello there", "greetings", "howdy",
    "what's up", "how's it going", "how are you doing", "nice to meet you",
    "pleased to meet you",
    "how's your day", "how's everything", "how's life", "how are things",
    "what's happening", "what's going on", "how's your day going", "how's your morning",
    "how's your afternoon", "how's your evening", "how's your night", "how's your week",
    "how's your weekend", "how's your day been", "how's your week been", "how's your weekend been",
    "how are you today", "how are you doing today", "how are you feeling today",
    "how are you this morning", "how are you this afternoon", "how are you this evening",
    "how are you this week", "how are you this weekend", "how are you feeling",
    "how are you holding up", "how are you getting on", "how are you getting along",
    "how are you keeping", "how are you managing", "how are you coping",
    "how are you today my friend", "how are you doing my friend", "how are you feeling my friend",
    "hey mark", "hi mark", "hello mark", "hey there mark", "hi there mark", "whats up mark"
    # Capability queries (15)
    "what can you do", "what are your capabilities", "what are your features",
    "what can you help me with", "what are your functions", "tell me what you can do",
    "what are your abilities", "what can you help with", "what do you do",
    "what are you capable of", "what can you help me with", "what are your skills",
    "what can you tell me", "what can you show me", "what can you teach me"
]

# Corresponding labels for training sentences (total: 161)
training_labels = [
    # Weather labels (8)
    "weather_query", "weather_query", "weather_query", "weather_query",
    "weather_query", "weather_query", "weather_query", "weather_query",
    # Web search labels (10)
    "web_search", "web_search", "web_search", "web_search", "web_search",
    "web_search", "web_search", "web_search", "web_search", "web_search",
    # Music labels (15)
    "play_music", "play_music", "play_music", "play_music", "play_music",
    "play_music", "play_music", "play_music", "play_music", "play_music",
    "play_music", "play_music", "play_music", "play_music", "play_music",
    # Time labels (8)
    "get_time", "get_time", "get_time", "get_time",
    "get_time", "get_time", "get_time", "get_time",
    # General knowledge labels (15)
    "general_knowledge", "general_knowledge", "general_knowledge", "general_knowledge",
    "general_knowledge", "general_knowledge", "general_knowledge", "general_knowledge",
    "general_knowledge", "general_knowledge", "general_knowledge", "general_knowledge",
    "general_knowledge", "general_knowledge", "general_knowledge",
    # Location-based labels (25)
    "location_query", "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query",
    # Additional location-based labels (12)
    "location_query", "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query", "location_query",
    "location_query", "location_query", "location_query", "location_query",
    # Personal questions labels (8)
    "personal_question", "personal_question", "personal_question", "personal_question",
    "personal_question", "personal_question", "personal_question", "personal_question",
    # Greetings labels (60)
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting", "greeting", "greeting", "greeting", "greeting",
    "greeting", "greeting"
    # Capability queries labels (15)
    "capability_query", "capability_query", "capability_query", "capability_query",
    "capability_query", "capability_query", "capability_query", "capability_query",
    "capability_query", "capability_query", "capability_query", "capability_query",
    "capability_query", "capability_query", "capability_query"
]

# Print exact counts for verification
#print(f"Total sentences: {len(training_sentences)}")
#print(f"Total labels: {len(training_labels)}")

# Verify that the number of sentences and labels match
assert len(training_sentences) == len(training_labels), f"Number of sentences ({len(training_sentences)}) does not match number of labels ({len(training_labels)})" 
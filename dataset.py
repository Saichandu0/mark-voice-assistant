# Comprehensive dataset of example sentences for various intents

# Time-related queries
time_queries = [
    "what time is it",
    "tell me the time",
    "current time please",
    "what's the time",
    "what time is it now",
    "can you tell me the time",
    "what's the current time",
    "what time do we have",
    "could you tell me what time it is",
    "time please",
    "hey what time is it",
    "what's the time right now",
    "what time is it currently",
    "do you know what time it is",
    "could you give me the time",
    "what's the time where you are",
    "time check please",
    "what time do you have",
    "can I know the current time",
    "what time is it over there"
]

# Location-based queries
location_queries = [
    # Restaurants and food
    "find me a restaurant",
    "suggest a good place to eat",
    "where can I eat",
    "I'm hungry",
    "find me a cafe",
    "suggest a coffee shop",
    "where can I get coffee",
    "I'm starving suggest me a good restaurant nearby",
    "I'm hungry find me a place to eat",
    "suggest me a good restaurant nearby",
    "find me a good place to eat nearby",
    "where can I find a good restaurant",
    "I need to eat something",
    "looking for a place to eat",
    "want to eat something",
    "where's the nearest restaurant",
    "can you find me a place to eat",
    "I need food suggestions",
    "where should I go for lunch",
    "what's a good place to eat around here",
    
    # Hotels and accommodation
    "find me a hotel",
    "suggest a place to stay",
    "where can I stay",
    "need a place to stay",
    "looking for accommodation",
    "where's a good hotel nearby",
    "can you find me a hotel",
    "need a place to sleep",
    "where can I book a room",
    "suggest a good hotel",
    
    # Shopping
    "find me a mall",
    "suggest a shopping place",
    "where can I shop",
    "where's the nearest shopping center",
    "need to go shopping",
    "where can I buy clothes",
    "looking for a shopping mall",
    "where's the best place to shop",
    "need to find a store",
    "where can I find a supermarket",
    
    # Entertainment and leisure
    "find me a park",
    "suggest a place to visit",
    "where can I go",
    "find me a gym",
    "suggest a fitness center",
    "where can I workout",
    "where's a good place to exercise",
    "looking for a park to walk",
    "where can I go for a run",
    "suggest a place to relax"
]

# Web search queries
web_search_queries = [
    "open Google",
    "search something",
    "google this",
    "search for",
    "look up",
    "search the web",
    "find information about",
    "look something up",
    "search online",
    "google search",
    "web search",
    "search the internet",
    "find on google",
    "look it up online",
    "search for me",
    "can you search",
    "please search",
    "do a search",
    "perform a search",
    "run a search"
]

# General knowledge queries
general_knowledge_queries = [
    # People
    "who is",
    "who was",
    "who are",
    "tell me about",
    "information about",
    "details about",
    "facts about",
    "who are the",
    "who is the",
    "who was the",
    "tell me who",
    "can you tell me about",
    "what do you know about",
    "give me information about",
    "who is this person",
    "who are these people",
    "tell me more about",
    "who is famous for",
    "who is known for",
    "who is the best",
    
    # Things and concepts
    "what is",
    "what are",
    "what was",
    "what does",
    "what do",
    "what makes",
    "what causes",
    "what happens when",
    "what is the meaning of",
    "what is the definition of",
    "what is the purpose of",
    "what is the history of",
    "what is the origin of",
    "what is the difference between",
    "what is the relationship between",
    "what is the significance of",
    "what is the importance of",
    "what is the process of",
    "what is the function of",
    "what is the role of"
]

# Greetings and basic interactions
greetings = [
    "hello",
    "hi",
    "how are you",
    "good morning",
    "good afternoon",
    "good evening",
    "hey there",
    "hi there",
    "hello there",
    "greetings",
    "howdy",
    "what's up",
    "how's it going",
    "how are you doing",
    "nice to meet you",
    "pleased to meet you",
    "good to see you",
    "how have you been",
    "what's new",
    "how's your day"
]

# Personal questions
personal_questions = [
    "what do you think about me",
    "do you like me",
    "what do you like about me",
    "how do you feel about me",
    "what's your opinion about me",
    "do you know me",
    "what do you know about me",
    "can you tell me about myself",
    "what do you think I should do",
    "what would you do if you were me",
    "do you understand me",
    "can you help me",
    "what can you do for me",
    "how can you help me",
    "what do you think I need",
    "do you have any advice for me",
    "what do you think about my situation",
    "can you give me some advice",
    "what would you suggest",
    "what do you recommend"
]

# Combine all queries into a single dataset
all_queries = {
    "time_queries": time_queries,
    "location_queries": location_queries,
    "web_search_queries": web_search_queries,
    "general_knowledge_queries": general_knowledge_queries,
    "greetings": greetings,
    "personal_questions": personal_questions
}

# Function to get all queries as a flat list
def get_all_queries():
    return [query for queries in all_queries.values() for query in queries]

# Function to get queries by category
def get_queries_by_category(category):
    return all_queries.get(category, []) 
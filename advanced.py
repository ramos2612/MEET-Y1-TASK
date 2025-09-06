import nltk
import wikipediaapi
import requests
import re  
from nltk.chat.util import Chat, reflections
#i wanted to use nltk but it has problems with the way it calls functions within the pairs responses


# wiki setup
user_agent = "test (ram.kador@gmail.com)"
wiki_wiki = wikipediaapi.Wikipedia(
    user_agent=user_agent,
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
    )

def getWiki(subject):
    page = wiki_wiki.page(subject)
    if page.exists():
        summary = page.summary[0:500] + "..."
        return f"{summary}\nTo read more: {page.fullurl}"
    else:
        return f"I couldn't find information about '{subject}'."

def getJoke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code != 200:
        return "I couldn't fetch a joke right now."
    return response.json()["setup"] + "\n" + response.json()["punchline"]

def getWeather(location):
    url = f"https://wttr.in/{location}?format=3"
    response = requests.get(url)
    if response.status_code != 200:
        return f"Couldn't get weather for {location}."
    return response.text

def getFact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    if response.status_code != 200:
        return "I couldn't fetch a fact right now."
    return response.json()["text"]

# Define patterns with their corresponding actions
patterns = [
    (r"(?:my name is|i am) (.*)", lambda match: f"Hello {match.group(1)}, nice to meet you!"),
    (r"(?:what is the weather in|weather in|temperature in) (.*)", lambda match: getWeather(match.group(1))),
    (r"what is the weather|temperature|weather", lambda match: getWeather("Israel")),
    (r"(?:explain|tell me about|what is|who is) (.*)", lambda match: getWiki(match.group(1))),
    (r"tell me a joke|tell me something funny|joke", lambda match: "joke: " + getJoke()),
    (r"tell me a fact|fun fact|fact", lambda match: "fact: " + getFact()),
]

def advanced():
    print("Hi! I'm your advanced chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye!")
            break
            
        if not user_input:
            continue
            
        response = None
        
        for pattern, action in patterns:
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                response = action(match)
                break
                
        if response is None:
            response = "I'm not sure how to respond to that."
            
        print(f"Bot: {response}")


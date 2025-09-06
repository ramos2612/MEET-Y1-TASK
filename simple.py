import random
def simple():
    user = input("Chat bot online")
    facts = ['2/3 is about 67%','52+15 is 67', 'i like the number 67%', 'september fourth is ']
    keywords = {'fact':['fact'],'help':['help','support'],'bye':['goodbye','bye'],'hi':['hi','hello'],'weather':['weather','forecast'],'time':['time','hour','minute'],'date':['date','day']}
    while not any(w in user.lower() for w in keywords['bye']):
        if any(w in user.lower() for w in keywords['hi']):
            print("Hello!")
        elif any(w in user.lower() for w in keywords['weather']):
            print("The forecast is sunny")
        elif any(w in user.lower() for w in keywords['time']):
            print("The time is 12:00")
        elif any(w in user.lower() for w in keywords['date']):
            print("The date is 9/7/2022")
        elif any(w in user.lower() for w in keywords['help']):
            print("What can i help you with?")
        elif any(w in user.lower() for w in keywords['fact']):
            print(random.choice(facts))
        else:
            print("I don't understand that")
        user = input("user message:")
    print("Bye!") 


#expandability: many of the responses can come from somewhere else using a api
#example: a weather api, time api and for the facts aswell
#also you can use chatbot apis like openai\gemini\grok\deepseek
#you can make the chat more interactive and feel more like a 2 sided conversation
#you can make it more personal by making the chat bot ask about you and also remember your responses

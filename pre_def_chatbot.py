#import the regular expression module to handle pattern matching
import re
#A dict to match keywords to predefines responses

responses={
    "hello":"Hi there! How can I assist you today?",
    "hi":"Hello! How can I help you?",
    "how are you":"I'm just a bot, but I'm doing great! How about you?",
    "want is your name":"I'm a chatbot created to assidt you",
    "help":"Sure, I'm here to help. What do you need assistance with?",
    "buy":"Goodbye! HAve a great day!",
    "thank you":"You're welcome! I'm happy to help.",
    "default":"I'm not sure I understand. Could you please rephrase?"
}

def chatbot_res(user_input):
    #convert user input to lower_case
    user_input=user_input.lower()
    for keyword in responses:
        if re.search(keyword,user_input):
            return responses[keyword]
    return responses["default"]
#main
def chatbot():
    print("Chatbot: Hello I'm here to assist you.(type'bye to exit')")
    while True:
        #get user input
        user_input=input("You: ")
        if user_input.lower()=='bye':
            print("Chatbot: Goodbye! Have a good day!")
            break        
        #response
        responses=chatbot_res(user_input)
        print(f"Chatbot: {responses}")

chatbot()
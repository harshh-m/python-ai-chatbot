import datetime
import time

name=input("Welcom, Entre Your name: ")
presenthour=datetime.datetime.now().hour

if 5<=presenthour<12 :
     print("Good Morning",name)
elif 12<=presenthour<17:
     print("Good Afternoon",name)
elif 17<=presenthour<21:
     print("Good Evening",name)
else:
     print("Good Night",name)


print("Welcome to CHatbot!")
print("You can ask me basic question, Type 'BYE' to exit from bot")

#Chatbot Memory Creation 

response ={
    "hii": "Hello! How can i assit you today?",
    "how are you":"I'm fine , thank you for asking!",
    "what is your name":"My Name is Chatbot",
    "motivate me":"Believe in yourself! You are capable of amazing things. Bug are the example of how to grow through adversity.",
    "what is python":"Python is a high-level, interpreted programming language known for its readability and versatility.",
    "what is ai":"Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
    "bye":"Goodbye! Have a great day ahead!"
}

#Method/Function to get response from chatbot
def getResponse(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in response:
     if eachkey in userQuestion:
        return response[eachkey]
    return  "SORRY!,I am in learning phase, I don't have answer to your question"

#Take User INput
while True:
    userInput=input("Please Ask Your question:")
    reply = getResponse(userInput)
    print("Bot Reply:",reply)
    time.sleep(5)

    if "bye" in userInput.lower():
        break
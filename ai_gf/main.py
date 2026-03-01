from brain import ask_gf
from memory import add_user, add_ai, get_history
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

personality = open("personality.txt", "r", encoding="utf-8").read()

print("GF is online 💕 (type 'bye' to exit)")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        break

    add_user(user)

    reply = ask_gf(user, get_history(), personality)

    add_ai(reply)

    print("GF:", reply)

    engine.say(reply)
    engine.runAndWait()
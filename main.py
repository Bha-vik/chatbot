

import random
from datetime import datetime


# Function to generate chatbot replies
def user_choice(message):
    text = message.lower()

    # Greetings
    if text in ["hii", "hello", "hey"]:
        replies = [
            "Hello there! (^^)",
            "Hi, nice to see you.",
            "Hey, how's it going?"
        ]
        return random.choice(replies)

    # chatbot name
    elif "name" in text:
        return "You can call me Kiki (^^)."

    # Asking  conditions
    elif "how are you" in text:
        answers = [
            "I'm doing fine (^^).",
            "Everything is good here.",
            "Doing well today."
        ]
        return random.choice(answers)

    # Time
    elif "time" in text:
        now = datetime.now().strftime("%I:%M %p")
        return f"The time now is {now}"

    # Date
    elif "date" in text:
        today = datetime.now().strftime("%d/%m/%Y")
        return f"Today's date is {today}"

    # Addition
    elif text.startswith("add"):
        try:
            values = text.split()

            first = int(values[1])
            second = int(values[2])

            return "Answer is " + str(first + second)

        except:
            return "Type like this: add 5 10"

    # Fun jokes
    elif "joke" in text or "jokes " in text:
        fun_jokes = [
            "Why did the boy bring a ladder to school? Because he wanted higher marks.",
            "Why did the phone go to sleep? Because its battery was tired.",
            "Why was the bicycle standing alone? Because it was two-tired."
        ]
        return random.choice(fun_jokes)

    # Exit 
    elif "bye" in text or "exit" in text:
        return "Goodbye. Have a nice day! (^^)"

    # Unknown Text
    else:
        return "Sorry, I could not understand (**)."


# Starting chatbot
print("================================")
print("        KIKI (^^) CHATBOT")
print("================================")


while True:

    user_input = input("You: ")

    bot_reply = user_choice(user_input)

    print("Kiki:", bot_reply)

    if user_input.lower() == "bye":
        break
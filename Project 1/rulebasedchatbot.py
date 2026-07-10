
# Simple Rule-Based Chatbot
# Project 1

print("Hello! I am Kathie, your friendly chatbot.")
print("Type 'bye' anytime to end the conversation.")

while True:
    user = input("\nYou: ").lower().strip()

    # Exit commands
    if user in ["bye", "exit", "quit", "goodbye"]:
        print("Kathie: Goodbye! Have a wonderful day. ")
        break

    # Greetings
    elif user in ["hi", "hello", "hey", "good morning", "good evening"]:
        print("Kathie: Hello! Nice to meet you.")

    # Asking chatbot's name
    elif "name" in user:
        print("Kathie: My name is Kathie. I'm a simple rule-based chatbot.")

    # Asking about health
    elif "how are you" in user:
        print("Kathie: I'm doing great! Thanks for asking. How about you?")

    # User feelings (Nested Conditions)
    elif "i am" in user:

        if "happy" in user:
            print("Kathie: That's wonderful! Keep smiling!")

        elif "sad" in user:
            print("Kathie: I'm sorry to hear that. I hope things get better soon.")

        elif "tired" in user:
            print("Kathie: Don't forget to take some rest and stay hydrated.")

        else:
            print("Kathie: Thanks for sharing how you're feeling.")

    # Time of day
    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print("Kathie: The current time is", current_time)

    # Asking about programming
    elif "python" in user:
        print("Kathie: Python is one of the easiest and most powerful programming languages!")

    # Asking for help
    elif "help" in user:
        print("Kathie: I can respond to greetings, emotions, my name, time, Python, and basic questions.")

    # Thank you
    elif "thank" in user:
        print("Kathie: You're welcome! Happy to help.")

    # Favorite color
    elif "favorite color" in user:
        print("Kathie: I like blue because it reminds me of technology and the sky!")

    # Joke
    elif "joke" in user:
        print("Kathie: Why do programmers prefer dark mode?")
        print("Kathie: Because light attracts bugs!")

    # Default response
    else:
        print("Kathie: Hmm... I don't understand that yet.")
        print("Kathie: Try saying 'hello', 'help', 'how are you', or 'tell me a joke'.")
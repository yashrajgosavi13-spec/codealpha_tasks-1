def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hii", "hey"]:
            print("Bot: Hi! How are you?")

        elif user in ["how are you"]:
            print("Bot: I'm fine, thanks!")

        elif user in ["what is your name", "your name"]:
            print("Bot: My name is basic Chatbot.")

        elif user in ["bye", "goodbye"]:
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
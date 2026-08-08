def chatbot():
    # Display the chatbot introduction
    print("Simple Chatbot")
    print("Type 'bye' to exit.\n")

    # Keep chatting until the user says bye
    while True:
        # Take user input and convert it to lowercase
        user = input("You: ").lower()

        # Check for common greetings
        if user in ["hello", "hi", "hii", "hey"]:
            print("Bot: Hello!")

        # Respond to a question about how the bot is doing
        elif user in ["how are you","how are you?"]:
            print("Bot: I'm fine, thanks!")

        # Respond when the user asks for the chatbot's name
        elif user in ["what is your name", "your name"]:
            print("Bot: My name is basic Chatbot.")

        # Exit the chatbot when the user says goodbye
        elif user in ["bye", "goodbye"]:
            print("Bot: Goodbye!")
            break

        # Default response for messages the bot does not understand
        else:
            print("Bot: Sorry, I don't understand.")


# Start the chatbot
chatbot()

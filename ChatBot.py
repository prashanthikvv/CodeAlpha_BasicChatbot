def chatbot():
    responses = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "how are you?": "I'm fine, thanks!",
        "bye": "Goodbye! Have a nice day!",
        "what's your name?": "I'm a simple chatbot!"
    }

    print("Chatbot: Hey! I'm your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in responses:
            print("Chatbot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Chatbot: I don't understand that yet.")

# Run the chatbot
chatbot()

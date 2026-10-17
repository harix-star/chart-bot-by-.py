print("🤖 Simple AI Chatbot")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! 👋")
    elif user == "how are you":
        print("Bot: I'm doing great! 😊")
    elif user == "what is your name":
        print("Bot: I'm your chatbot!")
    elif user == "bye":
        print("Bot: Goodbye! 👋")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")
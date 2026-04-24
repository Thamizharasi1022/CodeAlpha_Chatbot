print("Smart Chatbot (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hi! How can I help you?")
    
    elif "how are you" in user:
        print("Bot: I'm doing great!")
    
    elif "name" in user:
        print("Bot: I'm your Python Chatbot ")
    
    elif "thanks" in user or "thank you" in user:
        print("Bot: You're welcome!")
    
    elif "bye" in user:
        print("Bot: Goodbye!")
        break
    
    else:
        print("Bot: That's interesting! Tell me more")

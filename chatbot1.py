# Simple AI Chatbot (Without NLTK Download Issues)

import random

# Chatbot responses
responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?",
        "Greetings! I'm your AI chatbot."
    ],
    "bye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Chat again anytime!"
    ],
    "default": [
        "That's interesting! Tell me more.",
        "I'm listening! What else?",
        "Interesting! Tell me more about it."
    ]
}

def get_response(user_input):
    """Get response based on input."""
    text = user_input.lower().strip()
    
    # Check for greeting
    if any(word in text for word in ['hello', 'hi', 'hey']):
        return random.choice(responses["greeting"])
    
    # Check for goodbye
    if any(word in text for word in ['bye', 'goodbye', 'exit', 'quit']):
        return random.choice(responses["bye"])
    
    # Default response
    return random.choice(responses["default"])

def chat():
    """Main chat loop."""
    print("\n==== AI CHATBOT ====")
    print("Type 'bye' to exit")
    print("=" * 20)
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            print("AI: Please enter something!")
            continue
        
        response = get_response(user_input)
        print(f"AI: {response}")
        
        if any(word in user_input.lower() for word in ['bye', 'exit', 'quit']):
            print("\nAI Chatbot: Goodbye! Thanks for chatting!")
            break

if __name__ == "__main__":
    chat()
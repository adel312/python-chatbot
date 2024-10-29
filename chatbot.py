import re
import random

class Chatbot:
    def __init__(self):
        self.patterns = {
            r'hi|hello|hey': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! How are you doing?"
            ],
            r'how are you': [
                "I'm doing well, thanks for asking!",
                "I'm great! How about you?",
                "All good here! What can I do for you?"
            ],
            r'bye|goodbye': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Take care!"
            ],
            r'your name': [
                "I'm ChatBot, nice to meet you!",
                "You can call me ChatBot.",
                "ChatBot is my name!"
            ],
            r'help': [
                "I can chat with you about various topics. Just ask me something!",
                "I'm here to help! What would you like to know?",
                "Feel free to ask me anything!"
            ]
        }
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more about that.",
            "I'm still learning. Could you elaborate?",
            "That's something I'm not familiar with yet."
        ]

    def get_response(self, user_input):
        user_input = user_input.lower()
        
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        return random.choice(self.default_responses)

def main():
    chatbot = Chatbot()
    print("ChatBot: Hi! I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            print("ChatBot:", chatbot.get_response('bye'))
            break
            
        response = chatbot.get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
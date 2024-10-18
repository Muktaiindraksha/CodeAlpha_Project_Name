import random

# Define some common responses
greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Howdy!"]
farewells = ["Goodbye!", "See you later!", "Bye!", "Take care!", "Catch you later!"]
thank_responses = ["You're welcome!", "No problem!", "Glad to help!", "You're very welcome!"]
unknown_responses = ["I'm not sure I understand.", "Could you please rephrase?", "Sorry, I didn't get that."]

# Simple keyword-response pairs
responses = {
    "hello": greetings,
    "hi": greetings,
    "how are you": ["I'm just a bunch of code, but I'm doing fine!"],
    "what's your name": ["I'm a chatbot created to assist you."],
    "thank you": thank_responses,
    "bye": farewells,
}

def get_response(user_input):
    # Convert user input to lowercase for comparison
    user_input = user_input.lower()
    
    # Check if user input matches a keyword in responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # If no keyword is matched, return a generic response
    return random.choice(unknown_responses)

def chat():
    print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # If user types 'bye', end the chat
        if user_input.lower() == "bye":
            print(f"Chatbot: {random.choice(farewells)}")
            break
        
        # Get chatbot response and display it
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()








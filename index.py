# Dictionary containing some sample responses
responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm good, thank you! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't understand that."
}
# Function to get response to user input
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input matches any key in the responses dictionary
    for key in responses:
        if key in user_input:
            return responses[key]
    
    # If no match is found, return the default response
    return responses["default"]

# Main function to run the chatbot
def chat():
    print("Chatbot: Hello! How can I help you today? (Type 'bye' to exit)")
    
    while True:
        # Get user input
        user_input = input("User: ")
        
        # Check if user wants to exit
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        # Get and print response
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()

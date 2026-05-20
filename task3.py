# Basic Chatbot Program

def chatbot():
    print(" Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("chandu: ").lower()

        if user_input == "hello":
            print(" Chatbot: Hi!")
        elif user_input == "i am chandu":
            print(" Chatbot: Nice to meet you, Chandu!"
                  )
        elif user_input == "How are you":
            print(" Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print(" Chatbot: I am a simple Python chatbot.")

        elif user_input == "bye":
            print(" Chatbot: Goodbye!")
            break

        else:
            print(" Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
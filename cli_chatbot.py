#This is a basic chatbot that provides a command=line interface for interaction with the user. It has limited functionalities: telling jokes and fun facts, and can respond to a few predefined user queries.


import random 

#This is a function for asking and receiving basic questions and responses from the chatbot
def basic_questions():
    print("Aida:  You could ask me any of these: 'Are you a real person?, 'What's your name?', 'How are you feeling today? and a few more!")

    question = input("\nAida:  What would you like to know?   ").capitalize() #the capitalize() method enables the first letter of the user's input to be capitalized regardless of the case
    if question == "Are you a real person?":
        print("I'm a simple chatbot, and I don't have personal experiences or feelings.")
    elif question == "What's your name?":
        print("I'm called Aida and my aim is to be your aid.")
    elif question == "How are you feeling today?":
        print("I'm feeling ecstatic, thank you for asking.")
    elif question == "Recommend a book":
        print("I've got quite a few! You can check out Julie Kagawa's 'Shadow of the fox' or any of Dan Brown's books!")
    else:
        print("I'm sorry, I didn't understand that question.")

#This function displays a random joke from the list of jokes
def jokes():
    rand_jokes = [
        "What do you call a boomerang that doesn't come back? A stick.",
        "What do you call a pencil that's had too much to drink? Pencillated.",
        "I tried to catch some fog earlier. I mist.",
        "What kind of shoes do frogs wear? Open toad!",
        "Why don't eggs tell jokes? They might crack up.",
        "Why do programmers prefer dark mode? Because light attracts bugs."
    ]
    return random.choice(rand_jokes)   #the random module helps generate a random value from a list

#This function displays a random fact from the list of facts
def fun_facts():
    rand_facts = [
        "It is impossible for most people to lick their own elbow. (try it!)",
        "A crocodile cannot stick its tongue out.",
        "A shrimp's heart is in its head.",
        "Like fingerprints, everyone's tongue print is different.",
        "Rubber bands last longer when refrigerated.",
        "An ostrich's eye is bigger than its brain.",
        "Tigers have striped skin, not just striped fur."
    ]
    return random.choice(rand_facts)


#This is the main function that controls the chatbot's interactions and functionalities
def main():
    while True:
        print("\nAida:  HI THERE! I'M A BASIC CHATBOT AND I'D LOVE TO INTERACT WITH YOU! ")
        print("\nAida:  Would you like (me) to:  ")
        print("1. Ask some questions about me?")
        print("2. Tell a joke?")
        print("3. Share a fun fact?")
        print("Type 'ask questions' if 1, 'tell a joke' if 2 or 'share a fun fact' if 3.")
       
        user_input = input("\nUser:    ").capitalize()

        if user_input == "Ask questions":
            basic_questions()
        elif user_input == "Tell a joke":
            print(f"Aida: {jokes()}")
        elif user_input == "Share a fun fact":
            print(f"Aida: {fun_facts()}")
        elif user_input == "Bye":
            print("Aida:  GOODBYE!  HAVE A LOVELY DAY!")
            break
        else:
            print("Aida:  Invalid input")

if __name__ == "__main__":     
    main()   



    
    
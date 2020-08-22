# Write your code here
import random as rand
print("H A N G M A N")
  
def game():
    word_list = ["python", "java", "kotlin", "javascript"]
    word_choice = rand.choice(word_list)
    hyphen_list = []
    word_list = []
    for j in range(len(word_choice)):
        hyphen_list.append("-")
    count = 8
    while count > 0:
        print("\n"+"".join(hyphen_list))
        user_input =input("Input a letter: ")
        if user_input.islower() and user_input.isalpha() and len(user_input)==1:
            if user_input in word_choice and user_input not in word_list:
                for i in range(len(word_choice)):
                    if word_choice[i] == user_input:
                        hyphen_list[i] = user_input
                        word_list.append(user_input)
                        
            elif user_input in word_list:
                print("You already typed this letter")
                
            else:
                print("No such letter in the word")
                word_list.append(user_input)
                count=count-1
        elif len(user_input)!=1:
            print("You should input a single letter")
                    
        elif not user_input.islower() or not user_input.isalpha():
            print("It is not an ASCII lowercase letter")


    if "-" not in hyphen_list:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")    
def ask():
    answer = input("""Type "play" to play the game, "exit" to quit:""")
    if answer =="play":
        game()
    elif answer == "exit":
        print("Goodbye!")
    else:
        print("Please enter a valid response.")
        ask()
ask()  

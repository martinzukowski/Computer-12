#hangman

   
import random
import string
import time

words = ["Kwantlen", "Rai", "Zimmerman", "banana", "soccer", "pier", "baseball", "table", "chair", "plane", "computer", "water", "seahorse", "vision", "carpet", "model", "chicken", "barber", "potato", "vehicle", "nature", "surrey", "saxophone", "cheetah", "horse", "king"]
#  make sure kwantlen, rai, and zimmerman are not usable for  hangman
words.remove("Kwantlen")
words.remove("Rai")
words.remove("Zimmerman")

right_letter = ["Thats in there", "Nice guess", "You are lucky", "Smart man, very smart man..."]
# this line has random messages that will be shown if the user guesses correctly
wrong_letter = ["smh that was a bad guess", "Unlucky", "Lost a life!", "Better luck next time"]
# this line has random messages that will be shown if the user guesses incorrectly

# these are the hanman drawings
lives_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |        \ | /
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |        \ |
               |         / \\
               |
            """,
        2: """
              ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
            """,
        3: """
               ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        4: """
               ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        5: """
               ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        6: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        7: "",
    }

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word
    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print("You have " + str(lives) + " lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_dict[lives])
        print("Current word: " , " " .join(word_list))

        user_letter = input("Guess a letter: ").upper()
        time.sleep(1) #this line of code adds a 1 sec delay after a guess 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Your letter, " + user_letter + " is in the word. ")                

            else:
                lives = lives - 1  # takes away a life if wrong
                print("Your letter, " + user_letter + " is not in the word. " + random.choice(wrong_letter)) 
                #The line of code above prints a random phrase that was in the list, wrong_letter, because the user guessed incorrectly

        elif user_letter in used_letters:
            print("You have already used that letter. Guess a different letter.")

        else:
            print("Invalid letter. ")

    # this code is run when the word is guessed or when you run out of lives
    if lives == 0:
        print(lives_dict[lives])
        print("You lost. The word was", word)

    else:
        print("You guessed the right word. It was ", word)


print("""
            ___________
           | /        
           |/        
           |          
           |          
           |
        """) #this is the drawing shown before the game begins
hangman()

play_again = input("1 to play again, 2 to quit: ") #This code asks the user if they want to play again 

while play_again == "1":
    print("""
                ___________
               | /        
               |/        
               |          
               |          
               |
            """) # this is the drawing shown before the game begins
    hangman() #This code re plays hangman if the user wants to play again
    option = input("1 to play again, 2 to quit: ").lower()
    if option == "2":
        print ("You have succesfully quit") #this code ends the game when they want to quit
        
        break
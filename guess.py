# guess the number
import random 
def guess():
    randnum = random.randint(1,100)
    guess = -1
    while guess != randnum:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < randnum:
            print("Too low! Guess again.")
        elif guess > randnum:
            print("Too high! Guess again.")
    print (f"Got eeeeeeem!!! The number was {randnum}.")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (h) or too low (l), or correct (c)".lower())
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print ("The computer guessed your number, {guess}, correctly!")

while True:
    option = input("1 to guess, 2 to get guessed by the computer, Q to quit: ".lower())

    if option == "1":
        guess()
    elif option == "2":
        computer_guess(100)
    elif option == "q":
        print ("Quit.")
        break
    else:
        print("Invalid input")
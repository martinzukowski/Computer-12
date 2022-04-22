# quiz game
from winreg import REG_RESOURCE_REQUIREMENTS_LIST


print ("Welcome to my computer quiz! ")

option = input("Do you want to play? Yes/No ").lower()

if option != 'yes':
    quit()
print ("Okay lets play then! ")


def game():
    answer = input ("Spinach is high in which mineral? ").lower()
    score=0
    if answer == 'iron' :
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')

    answer = input('Whats the total number of dots on a pair of dice? ')
    if answer == '42':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')

    answer = input ('Which planet is closest to Earth? ').lower()
    if answer == 'venus':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')
    
    answer = input('What is the tallest mammal? ').lower()
    if answer == 'giraffe':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')
    
    answer = input('Which sign of the zodiac is represented by the ram? ').lower()
    if answer == 'aries':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')
    image1 = Image.open('violin.jpeg')
    image1.show('violin.jpeg')
    
    answer = input('How many strings does a violin have? ')
    if answer == '4':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')

    answer = input('What is the chemical symbol for hydrogen? ').lower()
    if answer == 'h':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')
        
    answer = input("Which animal is on the Porsche logo? ").lower()
    if answer == 'horse':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')
    image2 = Image.open('porsche.jpeg')
    image2.show('porsche.jpeg')
    
    answer = input('How many planets in the solar system? ')
    if answer == '8':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')

    answer = input("What disney movie is 'Elsa' in? ").lower()
    if answer == 'frozen':
        print('Correct! ')
        score += 1
    else:
        print('Incorrect! ')
    
    print('Your score: ' + str(score))
    print('You got ' + str((score/10)*100) + ' percent on this quiz. ') 

game()
option = input('Play again? Y/N: ').lower()
while True:
    if option == 'y':
        game()
        option = input('Play again? Y/N: ').lower()

    elif option == 'n':
        break
    else:
        print('Invalid response')

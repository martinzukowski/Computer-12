#madlibs game
from tkinter import E


noun = input("Noun: ")
adj = input("adjective: ")
place = input("Place: ")
number = int(input("Number: "))
verbing = input("Verb ending with ing: ")
body = input("Body part: ")
plural_noun = input("Plural noun: ")
#Option = input("Game 1,2, or 3? Press q to quit")
def madlib1():
    print ( "Once upon a time, " + noun + " was going to " + place  \
    + ". On the way there, it got hit by a swarm of " + plural_noun  \
    + ". After the incedent, " + noun + " felt very " + adj + ". To make itself feel better, " +\
    noun + " went to the store and bought " + str(number) + " drinks, and after that felt energized and started " + verbing + ". " +\
    noun + " was " + verbing + " so fast that its " + body + " fell off!. After this crazy experience " + noun + " went home. ")

def madlib2(): 
    print( "One morning, there was a " + noun + " who was very " + adj + ". So the " + noun + \
    " decided to find a " + place + " to eat a lot of " + plural_noun + ". Next it went to the club. Then the " \
    + noun + " kept " + verbing + " until it found " + str(number) + " " + body + "'s. Then finally it took a nap flying to Kwantlen Park")

def madlib3():
    print("I love " + noun + " because it is super " + adj + ". To find it, i have to go to " + place + " and when i get it " \
        + "I am so happy i fell like i can fly on " + str(number) + "clouds and start " + verbing + "everywhere. I would sell my "\
        + plural_noun + " to get it. I also love " + plural_noun + "just as much.")

option = input("Story 1, 2 ,3 or q for quit: ")

if option == "1":
    madlib1()

elif option == "2":
    madlib2()

elif option == "3":
    madlib3

elif option == "q":
    breakpoint

else:
    print ("Invalid input.")
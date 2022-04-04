#rock paper scissors lizard spock  
import random
countl = 0
countw = 0
countt = 0
def play(): 
    user = input("'r' for rock, 'p' for paper, 's' for scissors, 't' for spock, 'l' for lizard: ".lower())
    computer = random.choice(['r','p','s','t','l']).lower()

    if user == computer:
        global countt
        countt += 1
        return "U tied"

    if is_win(user, computer):
        global countw
        countw += 1
        return "Winner winner chicken dinner!"

    else: 
        global countl
        countl += 1
        return "you lost L"

def is_win(player, opponent):
    if (player == 'r' and opponent =='s') or(player == 'r' and opponent =='l') \
        or (player == 's' and opponent == 'p') or (player =='s' and opponent =='l')\
        or (player == 'p' and opponent == 'r') or (player == 'p' and opponent =='t')\
        or (player == 'l' and opponent == 't') or (player =='l' and opponent =='p') \
        or (player == 't' and opponent == 'r') or (player == 't' and opponent == 's'):
        return True

option = input("Keep playing? 1 to play 'Q' to quit: ").lower()

while option == "1":
    print(play())
    option = input("Keep playing? 1 to play 'Q' to quit: ").lower()
    if option == "q":
        print ("the endddddd)")
        print ("Win count: " + str(countw))
        print ("Lose count: " + str(countl))
        print ("Tie count: " + str(countt))

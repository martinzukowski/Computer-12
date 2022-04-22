# adventure choose game

name = input ("Enter name: ")
print('Welcome ', name, ' to this adventure!')

# First option
answer = input ('You are in the wrong neighbourhood in the town at night, and a gangster jumps out the side and starts chasing you, \
    you bust a quick turn down the road and you see a side alleyway and a main road, go (side) or (main)?: ').lower()

#Runs to the side alley
if answer == 'side':
    answer = input('You bust a left into the side street and run in between allyways between the tall buildings, you can \
        hear the gangster behind you, do you jump into the big dumpter bin to hide, or keep running further? (hide) or (run): ').lower()
    # hide in the dump
    if answer == 'hide':
        print('You hide but then you realize youre hiding in a dump with rats and you scream and jump out but then you get kilt by the gangster. ')
    # run further down
    elif answer == 'run':
        # last choice
        answer = input ('You run but you can see he is catching up, you hit a busy street with cars flying past, do you jaywalk and risk \
             it to run from the gangster? or do you turn around and fight? (jaywalk) or (fight)').lower()
        # fight the gangster
        if answer == 'fight':
            print('You throw a right hook and hit the gangster. He dies and you win!') # You win
        # jaywalk and run
        elif answer == 'jaywalk':
            print('You get scared and run away and risk it and cross the busy street. You think you are slick until a truck \
                runs over you and you die.') # You lose
    else:
        print('Invalid input' )
# run down the main street
elif answer == 'main':
    answer = input('You run down the main street and zig zag between obtacles but you trip and fall. The gangster catches up and is about to jump you, you find a brick, do you throw at his (face) or his (body)?').lower()
    # throw brick at face or body
    if answer == 'face':
        print ('You hit his face and he passes out, you run away and survive.') # win
    elif answer == 'body':
        print('He catches the brick and you die. ') # lose
    else:
        print('Invalid input' )
else:
    print('Invalid input. ')
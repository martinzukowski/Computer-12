
name = input ("Enter name: ")
print('Welcome ', name, ' to this adventure!')

answer = input ('You wake up and change, put on cool PANTS or comfortable SHORTS?: ').lower()

if answer == 'pants':
    answer = input('You put on the pants, you go to school and your crush waves and says "Nice pants." Do you WAVE \
        back or do NOTHING?: ').lower()
    if answer == 'wave':
        answer = input('You wave back, and your crush asks you on a date. Will you go? YES or NO: ').lower()
        if answer == 'yes':
            print('You go on the date, she turns out to be a scary monster and you die, the end. ')
        elif answer == 'no':
            print('You chose not to go on a date, next day at school you hear she was a monster. Good idea not to go!')
        else:
            print ('Invalid input')
    elif answer == 'nothing':
        print('Your crush didnt like you ignoring her, she reveals shes a monster and kills you. The end.')
    else:
        print('Invalid input')
elif answer == 'shorts':
    answer = input('You put on shorts and go to school. The bully sees you and makes fun of your shorts. BEAT him up or tell him to \
        see you in the FOREST after school?: ').lower()
    if answer == 'beat':
        print('You spring towards him and beat the bully, but the VPs catch you and expel you. The end.')
    elif answer == 'forest':
        print('You see him in the forest and have a dance battle. You smoke him because you have a mean dance arsenal. The end.')
    else:
        print('Invalid input')

else:
    print('Invalid input. ')
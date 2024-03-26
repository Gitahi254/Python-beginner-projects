name = input('What is your name?: ').lower()
print('Welcome', name, 'to the adventure of a lifetime!')

answer = input('You are on a dirt road. You have come to a junction and you are supposed to go either left or right. Which way would you pick? ').lower()

if answer == 'left':
    answer = input('You have come across a river on your left path. You can either walk around it or swim across it. What would you choose? Type "walk" to walk across or "swim" to swim across: ')
    if answer == 'swim':
        print('You swam across and were mauled by a hippo!')
    elif answer == 'walk':
        print('You walked for miles in the sun and ran out of water.')
    else:
        print('Not a valid option. Game over!')

elif answer == 'right':
    answer = input('You went right and came to a wobbly bridge. Do you want to cross it or go back? (cross/go back) ')
    if answer == 'go back':
        print('You went back to the start and got killed :(')
    elif answer == 'cross':
        answer = input('You went across the bridge and crossed successfully! You meet a stranger. Do you talk to him (yes/no). ')
        if answer == 'yes':
            print('You have been robbed and you lose the game :(')
        elif answer == 'no':
            answer = input('You decide to go on your own. It starts raining. You take out your map. Should you head to the mountains or to the valley? (mountain/valley) ')
            if answer == 'valley':
                print('You drowned and died in the mudslide :(')
            elif answer == 'mountain':
                answer = input('You made it to the mountain and survived the rain. What should you do first? Go hunt for food or look for shelter? (hunt/shelter)')
                if answer == 'hunt':
                    print('You were killed by a bear and died :(')
                elif answer == 'shelter':
                    answer = input('You are now safely sheltered from the rain. You have a matchstick and a lamp in the darkness. Which are you lighting first? (matchstick/lamp) ')
                    if answer == 'lamp':
                        print('You are unable to use your head!')
                    elif answer == 'matchstick':
                        print('Now you have lit your matchstick so you can light your lamp. You have won the game :)')

else:
    print('Not a valid option. Game over!')



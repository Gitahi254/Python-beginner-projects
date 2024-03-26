import random

top_of_range = input ('Type in a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

if top_of_range <= 0:
    print('Please type another number!')   
# else:
#     print('Please type a number!')


random_number = random.randint(0, top_of_range)
# print(random_number)
guesses=0

while True:
    guesses += 1  
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number!')
        continue

    if user_guess ==random_number:
        print('You garrit!')
        break
    elif user_guess > random_number:
         print('You were above the number.')
    else:
        print('You were below the number.')



print('You got in', guesses, 'tries:)')

   
#random.randint---
                # -------both include start points and end points
#random.randrange---

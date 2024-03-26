print ('Welcome to my quiz game!')

playing = input('Do you want to play the game? ')

if playing.lower() != 'yes':
    quit()

print ("Let's go boy! ;)")
score = 0
print('\n') #print new line

answer = input('Who was the first president of Kenya? ')
if answer == 'Jomo Kenyatta':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

answer = input('In which year did Kenya win independence? ')
if answer == '1963':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

answer = input('Nairobi is the capital city of Kenya. It is a Masai word, and what does it mean? ')
if answer == 'Place of cool waters':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

answer = input('In 1998 Kenya was in the international media after being attacked by terrorists in which over two hundred people lost their lives. Which diplomatic mission/office/embassy was bombed? ')
if answer == 'The American Embassy':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

answer = input("Mount Kenya is Kenya's highest mountain. Is it a dormant, extinct or active volcano? " )
if answer == 'extinct':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(') 
print('\n') #print new line

answer = input('Which is the largest county in Kenya? ')
if answer.lower() == 'turkana':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

answer = input('Which has the thickest fur of any mammal? ')
if answer.lower() == 'sea otter':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

answer = input(' How long is an elephant pregnant before it gives birth? ')
if answer == '22 months':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

answer = input("Which animal is known to spend most of it's day sleeping? ")
if answer.lower() == 'koala bear':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

answer = input('What is the only mammal that can not jump? ')
if answer == 'elephant':
    print ('Correct!')
    score +=1
else:
    print ('Sorry wrong answer :(')
print('\n') #print new line

print('You got ' + str(score)+ ' questions correct!')   
print("That's " +str((score/10) * 100)+ '%.!')   

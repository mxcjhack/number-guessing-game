import random
number_to_guess = random.randint(1,10)


print ('NUMBER GUESSING GAME')
print ('Rules:')
print ('1. Guess a number between 1 to 10\n2. You only have 4 tries')


guess = int(input('Guess the number:'))
number_of_guess = 0

while guess != number_to_guess:
    if guess < number_to_guess:
        print('guess higher')
    elif guess > number_to_guess:
        print('guess lower')
    
    if number_of_guess < 3:
        number_of_guess += 1
        guess = int(input('guess again:'))
    else:
        break

if number_of_guess != 4:
    print('YOU WON') 
else:
    print('GAME OVER')
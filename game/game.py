# prompt for positive int (n), if not reprompt
# generate random int between 1 - n inclusive
# guess the positive int, if not reprompt
    # if guess is small then generate 'Too small!'
    # if guess is largar then generate 'Too large!'
    # if guess right then generate 'Just right!'

from random import randint

done = False
while not done:
    n = input('Level: ')
    if n.isnumeric():
        try:
            guess = randint(1, int(n))
            done = True
        except ValueError:
            continue

done = False
while not done:
    guess_num = input('Guess: ')
    if guess_num.isnumeric():
        guess_num = int(guess_num)
        if guess_num == guess:
            print('Just right!')
            done = True
        elif guess_num < guess:
            print('Too small!')
        elif guess_num > guess:
            print('Too large!')

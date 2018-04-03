import random

player_name = raw_input('Enter name: ').capitalize()
print 'Hello, %s!' % player_name

rand_num = random.randint(1,100)
print '%s, I\'m thinking of a number between 1 and 100. \
\nTry to guess my number' % player_name


counter = 0
guess = True

while guess:
    player_guess = int(raw_input('Your guess?'))
    if isinstance(player_guess, int):
        if player_guess == rand_num:
            print 'Well done, %s! You found my number in %s tries!' % (player_name, counter)
            guess = False
        elif player_guess > rand_num:
            print 'Your guess is too high, try again.'
            counter += 1    
        elif player_guess < rand_num:
            print 'Your guess is too low, try again.'
            counter += 1
        else:
            print '%s! Check the range please!' % player_name
    else:
        print 'error'

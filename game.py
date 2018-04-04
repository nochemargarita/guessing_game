import random

player_name = raw_input('Enter name: ').capitalize()
print 'Hello, %s!' % player_name


print '%s, I\'m thinking of a number between 1 and 100. \
\nTry to guess my number' % player_name

# player guess as string
rand_num = random.randint(1,100)
counter = 0
lowest_counter = []
guess = True

# create a var lowest_counter = counter
# if counter < lowest_counter:
    # then lowest_counter is equal to counter
#create a condition that prompts the user to play again
    #if yes:
        #
while guess:
    
    player_guess = raw_input('Your guess?')
    try:
        player_guess = int(player_guess)

    except:
        print 'We spent an hour creating this message for you: PLEASE ENTER AN INTEGER!'

    if player_guess :
        if player_guess == rand_num:
            lowest_counter.append(counter)

            print 'Well done, %s! You found my number in %s tries!' % (player_name, counter)

            play_again = raw_input('Would you like to play again? Enter Y/N: ').upper()

            if play_again == 'Y':
                print 'Ok, let do it again.'
                counter = 0
                rand_num = random.randint(1,100)
                continue

            else:
                lowest_score = min(lowest_counter)
                print 'Your best score was %s!' % lowest_score
                print 'Ok bye!'
                exit() 

        elif player_guess > rand_num:
            print 'Your guess is too high, try again.'
            counter += 1    
        elif player_guess < rand_num:
            print 'Your guess is too low, try again.'
            counter += 1
        else:
            print '%s! Check the range please!' % player_name
   
        
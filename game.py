import random

number = random.randint(1, 99)

# Main program
player_name = input('Howdy, Whats your name? ')
number_of_guesses = 0
print(player_name, ", I'm thinking of a number between 1 and 100.")
print('Try to guess my number.')
print('Your guess?')

while number_of_guesses < 10:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low, try again')
        print('Your guess?')
    if guess > number:
        print('Your guess is too high, try again')
        print('Your guess?')
    if guess == number:
        break
if guess == number:
    print('Well done, ' + player_name + '! You found my number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))







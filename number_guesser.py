import random # You don't have to understand this statement

top_of_range = input("Type a number: ") # top_of_range is a variable that will determine the maximum range for the random number

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range:
        print('Please type a number larger than 0 next time.')

else:

random_number = random.randint(0, top_of_range) # random_number is a variable that will have a random number, the one to be guessed
guesses = 0

while True:

    user_guess = input("Make a guess: ")
    if user_guess:

    else:
        print('Please type a number next time.')

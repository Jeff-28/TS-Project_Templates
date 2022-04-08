import random

word_list = ['apple', 'bannana', 'lemon', 'fruit']  # List of words to play. You can edit this list.


'''get_word: function to return a random word from word_list'''
def get_word():
    word = random.choice(word_list)
    return word.upper()

'''
    print_letters_guessed: function to display the letters that have been guessed and the blank spaces for the letters missing
    word: a random word
    guesses: a list of user's guesses
'''
def print_letters_guessed(word, guesses):
    for letter in word:
        if letter.upper() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

'''play: function that will run the Hangman game from start to finish'''
def play():
    word            # this variable should have a random word to be guessed
    guesses = []    # this variable is a list that will hold the user's guesses
    done = False    # this variable should determine if the word was guessed or not
    lives = 7       # this variable represents the allowed errors for the user

    while :



        guess = input("Guess a letter: ")

        for letter in word:
            if letter.upper() not in guesses:
                done = False

    if   :
        print("You guessed the word! It was")
    else:
        print("Game Over! The word was")

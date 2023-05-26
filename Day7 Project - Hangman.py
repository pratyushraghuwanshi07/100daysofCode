#Python List Documentation - https://developers.google.com/edu/python/lists#for-and-in
#Importing Modules - https://www.askpython.com/python/python-import-statement
#Python Lists and Range documentation - https://developers.google.com/edu/python/lists#range

#Step 1 - Picking a random word from a list and checking if the user input letter is present in that word.
#Step 2 - Replacing the blank spaces with user guessed letters
#Step 3 - Checking if the user has won
#Step 4 - keeping track of players life
#Step 5 - Improving UI and adding ASCII character art

import random
import hangman_art
import hangman_words

print(hangman_art.logo)
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(hangman_art.stages[lives])
        print(f"{guess} is not a letter in the word!!!")
        lives -= 1
        if lives == -1:
            end_of_game = True
            print("You lose!!!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!!")

    
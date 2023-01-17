#Hangman Game
import random
from hangman_art import logo, stages
import hangman_words
from clear import clear

print(logo)

lives = 6
chosen_word = random.choice(hangman_words.word_list)
end_of_game = False
display = []
list_char = list(chosen_word)
word_length = len(chosen_word)
char_reduction = word_length
used_letters = []
#print(chosen_word)

for _ in range(word_length):
    display += "_"

while not end_of_game:
    user_guess = input("Enter a letter between a - z: \n ").lower()
    #clear()
    if user_guess in display:
        print("You've already used that letter!")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter

    if user_guess in used_letters:
        print(f"You've already used that letter!\n See {used_letters}")
    elif user_guess not in chosen_word:

        print(f"Your guess {user_guess} is not in the word. You lose a life.")
        lives -= 1
        used_letters += user_guess
        print(f"Incorrect Letters Used: \n ",used_letters)
        if lives == 0:
            end_of_game = True
            print(f"{stages[lives]}")
            print(f"\nThe word is {chosen_word}")
            print(f"\nYou LOST")
        

    print(f"{' '.join(display)} ")
    if "_" not in display and not lives == 0:
        end_of_game = True
        print(f"The word is {chosen_word}")
        print(f"\nYou WIN!!")
        

    print(stages[lives])
    print(f"{display} ")

    

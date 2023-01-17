# Hangman Game - MK Xinra 100 Days of Code Challenge - Udemy - london appbrewy
# CS-101 Final Project Version -
#Codecademy.com
import random
from hangman_art import logo, stages
import hangman_words
from clear import clear

clear()
print(logo)
class HangmanGame:
    def __init__(self):
        self.lives = 6
        self.chosen_word = random.choice(hangman_words.word_list)
        self.end_of_game = False
        self.display = []
        self.list_char = list(self.chosen_word)
        self.word_length = len(self.chosen_word)
        self.char_reduction = self.word_length
        self.used_letters = []
        for _ in range(self.word_length):
            self.display += "_"
            
    def play(self):
        while not self.end_of_game:
            user_guess = input("Enter a letter between a - z: \n ").lower()
            if user_guess in self.display:
                print("You've already used that letter!")

            for position in range(self.word_length):
                letter = self.chosen_word[position]
                if letter == user_guess:
                    self.display[position] = letter

            if user_guess in self.used_letters:
                print(f"You've already used that letter!\n See {self.used_letters}")
            elif user_guess not in self.chosen_word:

                print(f"Your guess {user_guess} is not in the word. You lose a life.")
                self.lives -= 1
                if self.lives < 0:
                    self.lives = 0
                self.used_letters += user_guess
                print(f"Incorrect Letters Used: \n ",self.used_letters)
                if self.lives == 0:
                    self.end_of_game = True
                    print(f"{stages[self.lives]}")
                    print(f"\nThe word is {self.chosen_word}")
                    print(f"\nYou LOST")
                    self.play_again()


            print(f"{' '.join(self.display)} ")
            if "_" not in self.display and not self.lives == 0:
                self.end_of_game = True
                print(f"The word is {self.chosen_word}")
                print(f"\nYou WIN!!")
                self.play_again()


            
            if self.lives > 0:
                print(stages[self.lives])
                print(f"{self.display} ")
            else:
                print('\nGAME OVER')
                


    def play_again(self):
        self.lives = 6
        self.chosen_word = random.choice(hangman_words.word_list)
        self.display = []
        self.list_char = list(self.chosen_word)
        self.word_length = len(self.chosen_word)
        self.char_reduction = self.word_length
        self.used_letters = []
        for _ in range(self.word_length):
            self.display += "_"
        play_again = input('\n PLAY AGAIN: Y or N \n ')
        clear()
        if 'y' in play_again.lower():
            self.end_of_game = False
            print(logo)
            self.play()
        else:
            print(logo)
            print('\nGood-Bye')       

game = HangmanGame()
game.play()

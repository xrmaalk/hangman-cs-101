"""
This file handles the difficulty level in the game.
Easy - 4 letter word
Medium - 5 letter word
Hard - 6 or more letter word
"""
import hangman_words


def select_difficulty():
    difficulty = input(
        'Select difficulty level (E - easy, M - medium, H - hard  \n').lower()
    word_list = hangman_words.WORD_LIST

    if 'e' in difficulty or difficulty == 'easy':
        difficulty_easy = [word for word in word_list if len(word) <= 4]
        return difficulty_easy
    elif 'm' in difficulty or difficulty == 'medium':
        difficulty_medium = [word for word in word_list if len(
            word) == 5]
        return difficulty_medium
    elif 'h' in difficulty or difficulty == 'h':
        difficulty_hard = [word for word in word_list if len(word) >= 6]
        return difficulty_hard
    else:
        print('Invalid entry, Please enter e, m or h to select difficulty level.')
        return select_difficulty()

"""Easy hangman game. This is my very first game, don't judge strictly)
Hangman rules: https://www.wikihow.com/Play-Hangman
v.1: Slightly improved the game by adding random word generation using the API"""
import time

import requests


def get_word():
    return ''.join([i for i in requests.get('https://random-word-api.herokuapp.com/word').text if i.isalpha()]).lower()


def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',

        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',

        '''
           --------
           |      |
           |      O
           |      
           |      
           |     
           -
        ''',

        '''
           --------
           |      
           |      
           |      
           |      
           |     
           -
        ''',
        '''
        
           |      
           |      
           |      
           |      
           |     
           -
        ''',
        '''




      


        '''
    ]
    return stages[tries]


def play(word):
    word_completion_list = list('_' * len(word))
    word_completion = ''.join(word_completion_list)
    guessed_letters = []
    guessed_words = []
    while True:
        tries = input('Enter the number of attempts (up to 8): ')
        if tries.isdigit() and 8 >= int(tries) >= 1:
            tries = int(tries)
            break
        else:
            print('Enter the number from 1 to 8.')
            time.sleep(0.2)
    print('Lets play hangman!')
    print('Condition at the moment:')
    print(display_hangman(tries))
    print(f'Hidden word: {word_completion.upper()}')
    while True:
        if tries == 0:
            return [False, word]
        input_word = input('Enter a letter or word:').lower()
        if not input_word.isalpha():
            print('How about a letter or a word?')
            continue
        if input_word == word:
            return [True, tries]
        if input_word in guessed_letters or input_word in guessed_words:
            print('This was before, enter another.')
            continue
        if len(input_word) == 1:
            if input_word in word:
                for i in range(len(word)):
                    if word[i] == input_word:
                        word_completion_list[i] = input_word
                        word_completion = ''.join(word_completion_list)
                print(f'The letter is in the hidden word! Hidden word:{word_completion.upper()}')
                guessed_letters.append(input_word)
                if word_completion == word:
                    return [True, tries]
            else:
                tries -= 1
                print(f"You didn't guess. Number of attempts left: {tries}")
                print(display_hangman(tries))
                guessed_letters.append(input_word)
        else:
            if len(input_word) != len(word):
                print(f'The hidden word consists of {len(word)} letters. Enter the full word or one letter.')
                continue
            else:
                tries -= 1
                print(f"You didn't guess the word. Number of attempts left: {tries}")
                print(display_hangman(tries))
                guessed_words.append(input_word)


def play_again(victory_flag, tries_count_or_word):
    if victory_flag:
        print(f'Congratulations! The word is completely guessed! Number of attempts left: {tries_count_or_word}.')
        print(f'Condition: {display_hangman(tries_count_or_word)}')
    else:
        print(f'Unfortunately, you lost. The hidden word was "{tries_count_or_word.upper()}".')
    print('Game over, want to start a new game? Enter "Yes" or "No"')
    while True:
        answer = input().lower()
        if answer != 'yes' and answer != 'no':
            print('Enter "Yes" or "No"')
            continue
        if answer == 'yes':
            print('Great, lets start new game..')
            return True
        else:
            print('Hope you had fun playing, have a nice day!')
            return False


def play_hangman():
    flag1 = True
    while flag1:
        flag, tries_or_word = play(get_word())
        flag1 = play_again(flag, tries_or_word)

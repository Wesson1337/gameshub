"""Entrance of the program"""
import hangman
import format_sec
import VigenereCipher
import time
import datetime
import snake
import roman


class Welcomer:
    def __init__(self):
        self.dict_of_games = {'Hangman': hangman.play_hangman,
                              'Snake': snake.play_snake}
        self.dict_of_utils = {'Vigenere cipher': VigenereCipher.use_vcipher,
                              'Seconds to human': format_sec.enter_format_duration,
                              'Roman numerals': roman.start_roman}
        self.welcome_count = 0
        self.start_datetime = datetime.datetime.now()

    def _welcome_anim(self):
        if self.welcome_count == 0:
            s = '''----------------------------------------------------------------------
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                Hi there! Welcome to gameshub!                  ---
---                   In this program you can:                     ---
---                1. Play mini-games (Enter 'Game')               ---
---               2. Use some utilities (Enter 'Util')             ---
---    3. Find out the time spent in the program (Enter 'Time')    ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                                                                ---
---                   Author: Wesson1337     v.1.0                 ---
----------------------------------------------------------------------'''
            lst = s.split('\n')
            for i in lst:
                time.sleep(0.15)
                print(i)

    def start_program(self):
        self._welcome_anim()
        while True:
            answer = input('Enter "Game", "Util" or "Time": ').lower()
            if answer == 'game' or answer == 'util':
                self._choose(answer)
            if answer == 'time':
                curr_time = (datetime.datetime.now() - self.start_datetime)
                print(f"Time spent in the program: {format_sec.format_duration(curr_time.seconds)}")

    def _choose(self, name):
        if name == 'util':
            chosen_dict = self.dict_of_utils
        else:
            chosen_dict = self.dict_of_games
        while True:
            print(f'List of {name}s:')
            for i in enumerate(chosen_dict):
                print(f"{i[0] + 1}. {i[1]}")
            answer = input(f'Enter name or number of the {name} or "quit": ').lower()
            for digit, key in enumerate(chosen_dict):
                if answer == str(digit + 1) or answer == key.lower():
                    chosen_dict[key]()
                    return None
            if answer == 'quit' or answer == 'q':
                return None
            else:
                print("I don't understand you :(")


if __name__ == '__main__':
    Welcomer().start_program()

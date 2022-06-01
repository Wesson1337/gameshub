"""Decoding and encoding words into Vigenere cipher. It takes two argument:
the first is a key and second is arbitrary alphabet. Funcs take one argument - text,
which you want to encode/decode, return encoded/decoded text. """

import time


def is_valid(text, alphabet):
    for i in text:
        if i not in alphabet and i.isalpha():
            return False
    return True


class VigenereCipher:

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encrypted = []
        alphabet = self.alphabet
        key = self.key
        alphabet_len = len(alphabet)
        key_len = len(key)
        for i, char in enumerate(text):
            encrypted.append(alphabet[(alphabet.index(char) + alphabet.index(
                key[i % key_len])) % alphabet_len] if char in alphabet else char)
        return ''.join(encrypted)

    def decode(self, text):
        encrypted = []
        key = self.key
        key_len = len(key)
        alphabet = self.alphabet
        for i, char in enumerate(text):
            encrypted.append(
                alphabet[(alphabet.index(char) - alphabet.index(key[i % key_len]))] if char in alphabet else char)
        return ''.join(encrypted)


def use_vcipher():
    prev_key = 'pizza'
    prev_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        print('If you want quit, enter "quit".')
        time.sleep(0.2)
        new_key = input('Enter a new key or leave the existing one by entering "skip" (Default key - pizza): ').lower()
        new_alphabet = input('Enter a new alphabet or leave the existing one by entering "skip" (Default alphabet - '
                             'English): ').lower()
        if new_key == 'quit' or new_alphabet == 'quit':
            return None
        if new_key == 'skip' or new_key == '':
            new_key = prev_key
        if new_alphabet == 'skip' or new_alphabet == '':
            new_alphabet = prev_alphabet
        prev_key, prev_alphabet = new_key, new_alphabet
        new_cipher = VigenereCipher(new_key, new_alphabet)
        while True:
            message = input('Enter the message you want to decode or encode: ').lower()
            if not is_valid(message, new_alphabet):
                print(f'Message not in alphabet, current alphabet: "{new_alphabet}"')
                continue
            break
        while True:
            answer = input('Enter what you want: "decode" or "encode": ').lower()
            if answer == 'decode':
                print(f"Your decoded message: {new_cipher.decode(message)}")
                break
            if answer == 'encode':
                print(f"Your encoded message: {new_cipher.encode(message)}")
                break
            else:
                print("I don't understand you :(")

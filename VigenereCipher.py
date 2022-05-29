def is_valid(text, alphabet):
    for i in text:
        if i not in alphabet and i.isalpha():
            return False
    return True


class VigenereCipher(object):
    """Class for decoding and encoding words into Vigenere cipher. It takes two argument: \
the first is a key and second is arbitrary alphabet. Funcs take one argument - text, \
which you want encode/decode, return encoded/decoded text. """

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.alphabet_dict = {j: k for k, j in enumerate(self.alphabet)}
        self.alphabet_dict_reverse = {k: j for k, j in enumerate(self.alphabet)}

    def encode(self, text):
        if not is_valid(text, self.alphabet):
            return text
        encode_key = (self.key * len(text))[:len(text)]
        s = ''
        lst = []
        for i, j in zip(text, encode_key):
            if i.isalpha():
                lst.append((self.alphabet_dict[i] + self.alphabet_dict[j]) % len(self.alphabet))
            else:
                lst.append(i)
        for i in lst:
            if str(i).isdigit():
                s += self.alphabet_dict_reverse[i]
            else:
                s += i
        return s

    def decode(self, text):
        if not is_valid(text, self.alphabet):
            return text
        encode_key = (self.key * len(text))[:len(text)]
        s = ''
        lst = []
        for i, j in zip(text, encode_key):
            if i.isalpha():
                x = self.alphabet_dict[i] - self.alphabet_dict[j]
                if x < 0:
                    x += len(self.alphabet)
                lst.append(x)
            else:
                lst.append(i)
        for i in lst:
            if str(i).isdigit():
                s += self.alphabet_dict_reverse[i]
            else:
                s += i
        return s


if __name__ == '__main__':
    print(VigenereCipher.__doc__)

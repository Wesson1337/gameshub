import time

roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
              'XC': 90,
              'CD': 400, 'CM': 900}


def to_roman(val):
    s = ''
    s += 'M' * (val // 1000)
    if val // 100 % 10 == 9:
        s += 'CM'
    elif val // 100 % 10 == 4:
        s += 'CD'
    elif val // 100 % 10 >= 5:
        s += 'D' + 'C' * (val // 100 % 10 - 5)
    else:
        s += 'C' * (val // 100 % 10)
    if val // 10 % 10 == 9:
        s += 'XC'
    elif val // 10 % 10 == 4:
        s += 'XL'
    elif val // 10 % 10 >= 5:
        s += 'L' + 'X' * (val // 10 % 10 - 5)
    else:
        s += 'X' * (val // 10 % 10)
    if val % 10 == 9:
        s += 'IX'
    elif val % 10 == 4:
        s += 'IV'
    elif val % 10 >= 5:
        s += 'V' + 'I' * (val % 10 - 5)
    else:
        s += 'I' * (val % 10)
    return s


def from_roman(roman):
    s = roman
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman_dict:
            num += roman_dict[s[i:i + 2]]
            i += 2
        else:
            num += roman_dict[s[i]]
            i += 1
    return num


def start_roman():
    print('Enter "quit" to quit.')
    time.sleep(1)
    while True:
        answer = input('What do you want? Translate into Roman numerals (enter "into") or translate from Roman '
                       'numerals (enter "from")? ')
        if answer == 'q' or answer == 'quit':
            return None
        elif answer == 'into':
            while True:
                num = input('Enter the number up to 3999: ').lower()
                if num == 'q' or num == 'quit':
                    return None
                elif num.isdigit() and 3999 >= int(num) >= 0:
                    print(f"Your Roman number: {to_roman(int(num))}")
                    break
                else:
                    print('I dont understand you :(')
        elif answer == 'from':
            while True:
                flag = True
                num = input('Enter the roman up to 9999: ').lower()
                if num == 'q' or num == 'quit':
                    return None
                for i in num:
                    if i.upper() not in roman_dict.keys():
                        flag = False
                if flag:
                    print(f"Your decimal number: {from_roman(num.upper())}")
                    break
                else:
                    print('I dont understand you :(')
        else:
            print('I dont understand you :(')


if __name__ == '__main__':
    start_roman()

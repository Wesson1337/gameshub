"""Converts number of seconds to human representation without any unnecessary words \
and with 's' at the end for plural date."""

import time


def format_duration(seconds):
    diction = {'year': seconds // (86400 * 365), 'day': seconds // 86400 % 365,
               'hour': seconds // 3600 % 24, 'minute': seconds // 60 % 60,
               'second': seconds % 60}
    lst = []
    for i in diction:
        if diction[i] and diction[i] != 1:
            lst.append(f'{diction[i]} {i}s')
        elif diction[i] == 1:
            lst.append(f'{diction[i]} {i}')
    if len(lst) >= 2:
        lst[-1] = f'and {lst[-1]}'
        pop = lst.pop()
        return f"{', '.join(lst)} {pop}"
    if lst:
        return lst[0]
    return 'now'


def enter_format_duration():
    while True:
        print('If you want quit, enter "quit".')
        time.sleep(0.2)
        x = input('Please, enter number of seconds: ')
        if x == 'quit':
            return None
        if x.isdigit():
            print(f'Formatted date: {format_duration(int(x))}')
        else:
            print('This is not a number of seconds')

### Gameshub
_____
**Gameshub** is the easiest script to enter any game or utility you want. It has no GUI in version 1.0.

If you want to add your own game or utility, just add to the file **'main.py'** in the class dictionary the name of the program in 
camelcase and a function that starts your program:

```python
self.dict_of_games = {'Hangman': hangman.play_hangman,
                      'Snake': snake.play_snake}
self.dict_of_utils = {'Vigenere cipher': VigenereCipher.use_vcipher,
                      'Seconds to human': format_sec.enter_format_duration}
```
#### In version 1.0 Gameshub can provide two games:
+ snake
+ hangman

#### And two utilities:
+ Vigener cipher
+ Seconds to human
+ Roman numerals

#### To run program just run main.py
___
P.S. This is my very first project, and I think in the future I will be ashamed of it :)


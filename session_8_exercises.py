"""
Zachary Bedrosian
Session 7 Exercises
9.28.2017
"""

key = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}

key_reverse = {
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j',
    10:'k',
    11:'l',
    12:'m',
    13:'n',
    14:'o',
    15:'p',
    16:'q',
    17:'r',
    18:'s',
    19:'t',
    20:'u',
    21:'v',
    22:'w',
    23:'x',
    24:'y',
    25:'z'
}

def rotate_word(word, displace_by):
    new_word = ''
    for letter in word:
        lower_case = False
        if letter.islower():
            lower_case = True
        letter = letter.lower()
        letter_number = key[letter]
        letter_number += displace_by
        if letter_number >= 26:
            letter_number -= 26
        letter = key_reverse[letter_number]
        if not lower_case:
            letter = letter.upper()
        new_word += letter
    return new_word




print(rotate_word('Zachary', 3))

import string

VOWELS = 'aeiouAEIOU'
CONSONANTS = [c for c in string.ascii_letters if c not in VOWELS]

def num_vowels(s):
    vowels = 0
    for c in s:
        if c in VOWELS:
            vowels += 1
    return vowels

def num_consonants(s):
    consonants = 0
    for c in s:
        if c in CONSONANTS:
            consonants += 1
    return consonants

s = input('Enter string: ')
print('Vowels:', num_vowels(s))
print('Consonants:', num_consonants(s))

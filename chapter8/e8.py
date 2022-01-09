'''
Write a program with a function that accepts a string as an argument
and returns a copy of the string with the first character of each
sentence capitalized. For instance, if the argument is "hello. my name
is Joe. what is your name?" the function should return the string
"Hello. My name is Joe. What is your name?" The program should let the
user enter a string and then pass it to the function. The modified
string should be displayed.
'''


import re


def capitalize_sentence(input_sentence):
    # Find first non-whitespace character, if one exists
    match = re.search(r'(\S)', input_sentence)

    if match:
        capital_char = match.group(1).upper()
        # Replace the first (and only the first)
        # occurrence of a non-whitespace character with
        # its capitalization
        output_sentence = re.sub(r'\S', capital_char,
                                 input_sentence, count=1)
    else:
        # No non-whitespace characters, so no
        # capitalization to be done
        output_sentence = input_sentence

    return output_sentence


def capitalizer(s):
    builder = []    # List holding substrings
    index = 0       # Position in string
    stop = False    # Flag to control loop

    while not stop:
        # Two captures: one for not sentence-ending
        # puntuation, and then one for sentence-ending
        # puntuation. Both need to be captured. The first
        # group is capitalized, and the second group (the
        # ending punctuation) is placed in the proper place
        # in the output string.
        #
        # The first capture must use * because the first
        # group can be empty (as in the case of the string
        # '.foo'). The second capture must use + because
        # the ending punctuation must be one or more
        # characters long.
        match = re.search(r'([^.!?]*)([.!?]+)', s[index:])

        if match:
            input_sentence = match.group(1)
            punctuation = match.group(2)
            index += match.end(2)  # Update index
        else:
            # No match, so this "sentence" is the last
            # one to be processed
            stop = True
            # The remainder of the string is the last
            # "sentence"
            input_sentence = s[index:]
            # No punctuation
            punctuation = ''

        output_sentence = capitalize_sentence(input_sentence)
        builder.append(output_sentence)
        builder.append(punctuation)

    # Concatenate output list to get back a string
    return ''.join(builder)


def main():
    print('Running assertions.')
    assert capitalizer('hello. my name is Joe. what is your name?') == 'Hello. My name is Joe. What is your name?'
    assert capitalizer('foo bar. !? 8baz.buz quz ') == 'Foo bar. !? 8baz.Buz quz '
    assert capitalizer('.foo bar.') == '.Foo bar.'
    assert capitalizer('.baz!? bar.e') == '.Baz!? Bar.E'
    print('All assertions passed.')


if __name__ == '__main__':
    main()

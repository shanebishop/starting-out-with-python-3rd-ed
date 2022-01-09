import re


def get_sentence(s):
    builder = []
    index = 0
    first_word = True

    while True:
        match = re.search(r'([A-Z])([^A-Z]*)', s[index:])

        if not match:
            break

        if first_word:
            # Keep first letter as capital
            first_letter = match.group(1)
            # The next word will not be the first word
            first_word = False
        else:
            # Convert first letter to lowercase
            first_letter = match.group(1).lower()

        word = first_letter + match.group(2)
        index += match.end(2)  # Update index

        builder.append(word)

    return ' '.join(builder)

assert get_sentence('StopAndSmellTheRoses') \
    == 'Stop and smell the roses'
assert get_sentence('WhereAreYouGoing,CanICome?') \
    == 'Where are you going, can i come?'
print('All assertions passed.')

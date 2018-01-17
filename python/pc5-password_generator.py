import random


def generate_password():
    # Selects three random words from a provided file of words
    # and concatenates them into a single string.
    # The code to read in the data from the file is already in the starter code,
    # you will need to build a password out of these parts.

    word_file = "words.txt"
    word_list = []
    password = ''

    # fill up the word_list
    with open(word_file, 'r') as words:
        for line in words:
            # remove white space and make everything lowercase
            word = line.strip().lower()
            # don't include words that are too long or too short
            if 3 < len(word) < 8:
                word_list.append(word)

    for i in range(3): password += str(word_list[random.randrange(0, len(word_list))])
    return password

    # OR
    # return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

    # OR
    #    return str().join(random.sample(word_list,3))


print(generate_password())

import csv

def get_dictionary(initial, length):
    """Creates a list of all words beginning with a particular letter."""
    filename = 'dictionary/' + initial + '_words.csv'
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        words = []
        for row in reader:
            word = row[0]
            if len(word) == length:
                words.append(word)
    return words

def get_fixed_letters(working_position, square_words):
    """Returns fixed letters to search against."""
    fixed_letters = ''
    for y in range(working_position):
        letters = list(square_words[y])
        try:
            letter_add = letters[working_position]
        except IndexError:
            letter_add = 'n'
        else:
            fixed_letters += letter_add
            fixed_letters.strip()
    return fixed_letters
        

import csv

def get_dictionary(initial, length):
    """Creates a list of all words beginning with a particular letter."""
    filename = initial + ' Words.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        words = []
        for row in reader:
            word = row[0]
            if len(word) == length:
                words.append(word)
    return words
        

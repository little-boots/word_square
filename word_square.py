from dictionary import get_dictionary

#Take input of the starting word
seed_word = input('Enter a word: ')
seed_word = seed_word.lower()

#Break the seed word into individual letters
initials = list(seed_word)

#get the length for words that will fit the square
length = len(seed_word)

#Make a dictionary of appropriate length words for each initial
word_lists = []
for x in range(length):
    word_list = get_dictionary(initials[x], length)
    word_lists.append(word_list)

#Build the word square by recursively cycling through the lists

#Print the word square 

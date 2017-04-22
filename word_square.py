from dictionary import get_dictionary, get_fixed_letters

run = True
while run == True:

    #Ask for a seed word
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

    #make a list to hold the solution words
    square_words = []
    square_words.append(seed_word)

    #make a list to hold partially consumed test words
    word_list_shelf = []
    word_list_shelf.append('null')

    #initialize other variables
    working_position = 1
    square_solved = False
    last_test = ''
    test_strip = 'init'

    fixed_letters = get_fixed_letters(working_position, square_words)

    word_list = word_lists[working_position].copy()

    #Build the word square by recursively cycling through the lists
    while working_position < length:
        try:
            test_word = word_list.pop()
        except IndexError:
            if working_position > 1:
                working_position -= 1
                word_list = word_list_shelf[working_position]
                fixed_letters = get_fixed_letters(working_position, square_words)
            elif working_position == 1:
                print('\nNo valid word_square exists.\nThis all I could do:\n')
                for word in square_words:
                    print(word)
                working_position = length + 1
        else:
            last_test = test_strip
            test_strip = test_word[:working_position]
            if test_strip != last_test:
                if test_strip == fixed_letters:
                    try:
                        square_words[working_position] = test_word
                    except IndexError:
                        square_words.append(test_word)
                    try:
                        word_list_shelf[working_position] = word_list
                    except IndexError:
                        word_list_shelf.append(word_list)
                    working_position += 1
                    if working_position < length:
                        fixed_letters = get_fixed_letters(working_position, square_words)
                        word_list = word_lists[working_position].copy()
                    else:
                        square_solved = True
                        
    #Print the word square
    if square_solved == True:
        print('\nSquare Solved!!!\n')
        for z in range(length):
            print(square_words[z])

    try_again = input('\nTry again?\n(y/n):  ')
    try_again.lower()
    if try_again == 'n':
        run = False

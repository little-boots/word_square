from dictionary import get_dictionary, get_fixed_letters

#Ask for initial seed word
seed_word = input('Enter a word: ')
seed_word = seed_word.lower()

run = True
while run == True:

    #Break the seed word into individual letters
    initials = list(seed_word)

    #Get the length for words that will fit the square
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
    test_strip = 'init'
    solutions = 0

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
                if solutions == 0:
                    print('\nNo valid word_square exists.')
                else:
                    print('\nOperation Complete.')
                working_position = length + 1
        else:
            test_strip = test_word[:working_position]
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
                if working_position == length:
                    #square_solved = True
                    solutions += 1
                    solution_filename = 'solutions/' + seed_word + '_word_squares.txt'
                    with open(solution_filename, 'a') as solution_file:
                        for v in range(length):
                            solution_file.write(square_words[v].upper() + '\n')
                        solution_file.write('\n\n')
                    print(str(solutions) + ' solution(s) found!!!')
                    working_position -= 1  
                else:
                    fixed_letters = get_fixed_letters(working_position, square_words)
                    word_list = word_lists[working_position].copy()
                        
    #Print the word square
    #All this will have to be changed for "find all"
    #if square_solved == True:
    #    print('\nSquare Solved!!!\n')
    #    for z in range(length):
    #        print(square_words[z].upper())

    #Report action
    print('Check the solutions folder.')

    #Ask to go again
    seed_word = input('\nEnter a new word?\n(Or "q" to quit):  ')
    seed_word.lower()
    if seed_word == 'q':
        run = False

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
    word_list_shelf.append('null')  #seed word doesn't consume a list, so this is a placeholder

    #initialize other variables
    working_position = 1
    test_strip = 'init'
    solutions = 0

    #get the first fixed letter
    fixed_letters = get_fixed_letters(working_position, square_words)
    #grab the first set of test words to cycle through
    word_list = word_lists[working_position].copy()

    #Build word squares by recursively cycling through the lists
    while working_position < length:
        try:
            #grab a word
            test_word = word_list.pop()  
        #if there's no word to grab,
        except IndexError:	
            #if this isn't a final, fatal failure,
            if working_position > 1:	
                #back up a row.
                working_position -= 1	
                #grab the partially consumed word list from earlier
                word_list = word_list_shelf[working_position]	
                #get the fixed letters to check against
                fixed_letters = get_fixed_letters(working_position, square_words)	
            #if this is a final failure (since working_position 0 is the seed word)
            elif working_position == 1:	
                #if this is a total failure (no solutions found)
                if solutions == 0:	
                    print('\nNo valid word_square exists.')
                #otherwise, report the action taken
                else:
                    print('\nOperation Complete.\nCheck the solutions folder.')
                #break out of the recursive loop
                working_position = length + 1	
        else:
            #grab a slice the same length as current fixed letters to check against
            test_strip = test_word[:working_position]	
            #see if the slice matches the fixed letters
            if test_strip == fixed_letters:	
                try:	
                    #maybe there's a solution word already in this spot
                    square_words[working_position] = test_word
                except IndexError:	
                    #if not, make a new one
                    square_words.append(test_word)
                try:
                    #put the partially consumed list on the shelf, if a spot exists
                    word_list_shelf[working_position] = word_list
                except IndexError:
                    #if no spot exists, make a new one
                    word_list_shelf.append(word_list)
                #move to the next row
                working_position += 1
                #if this is a total solution (a valid word in the final row)
                if working_position == length:	
                    #increment the solutions count
                    solutions += 1
                    #make a filename indicating the seed word
                    solution_filename = 'solutions/' + seed_word + '_word_squares.txt'
                    #open the file in 'append mode' as an object to work with
                    with open(solution_filename, 'a') as solution_file:
                        #make a loop that will run once for each solution word
                        for v in range(length):
                            #write each solution word on its own line
                            solution_file.write(square_words[v].upper() + '\n')
                        #write two blank lines after each complete solution for readability
                        solution_file.write('\n\n')
                    #give feedback in the command line to show progress
                    print(str(solutions) + ' solution(s) found!!!')
                    #drop back down so that remaining words in the list can be checked
                    working_position -= 1  
                #if this isn't a total solution
                else:
                    #get new fixed letters to check against for this row
                    fixed_letters = get_fixed_letters(working_position, square_words)
                    #get a fresh word list to cycle through for this position 
                    word_list = word_lists[working_position].copy()

    #Ask to go again
    seed_word = input('\nEnter a new word?\n(Or "q" to quit):  ')
    seed_word.lower()
    if seed_word == 'q':
        run = False

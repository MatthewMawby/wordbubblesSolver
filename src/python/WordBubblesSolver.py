#Written by: Matthew Mawby
#Version 1.0

import enchant

#------------------------------------------------------------------FUNCTIONS CREATED AND DEFINED HERE------------------------------------------------------------------

#A recursive search algorithm that finds words of a given length in a 2d table of letters
#by treating the letters as nodes with edges to all the letters in the table immediately surrounding
#the given letter.
#results is a set of strings containing words that are found
#word_table is a list of strings that compose the letters and their positions given by wordbubbles
#word_length is the target length of a word
#curr_length is the length of the current recursive branch
#visited is a set of tuples representing visited already visited letters in the current branch
#prev_string is a string keeping track of the previously visited letters and their order of the current branch
#curr_coord is a tuple of the coordinate in word_table of the letter currently being visited
#dict is a spell checker that is used to see if generated strings are english words
def find_words(results, word_table, word_length, curr_len, visited, prev_string, curr_coord, dictionary):
    #end branches that lead to empty spaces ('-' metacharacter)
    if word_table[curr_coord[0]][curr_coord[1]] == '-':
        return

    #update the string
    prev_string = prev_string+word_table[curr_coord[0]][curr_coord[1]]
    #base case, end the recursive branch when you've reached a word of the target length
    if curr_len == word_length:
        if prev_string not in results and dictionary.check(prev_string.lower()):
            results.add(prev_string)
        return

    #If the branch doesn't terminate, update information and recurr
    #makes a copy of the visited set (since sets behave as pass by reference) and adds the current coordinate to visited
    update_visited = set([])
    update_visited.add(curr_coord)
    update_visited = update_visited.union(visited)

    x_coord = curr_coord[0]
    y_coord = curr_coord[1]
    columns = len(word_table[0])
    rows = len(word_table)

    #attempt to recurr at all surrounding spaces that are in bounds and that haven't been visted yet
    if x_coord-1 >= 0 and y_coord-1 >= 0:
        if (x_coord-1, y_coord-1) not in visited:
            find_words(results, word_table, word_length, curr_len+1, update_visited, prev_string, (x_coord-1, y_coord-1), dictionary)
    if x_coord-1 >= 0:
        if (x_coord-1, y_coord) not in visited:
            find_words(results, word_table, word_length, curr_len+1, update_visited, prev_string, (x_coord-1, y_coord), dictionary)
    if x_coord-1 >= 0 and y_coord+1 < columns:
        if (x_coord-1, y_coord+1) not in visited:
            find_words(results, word_table, word_length, curr_len+1, update_visited, prev_string, (x_coord-1, y_coord+1), dictionary)
    if y_coord+1 < columns:
        if (x_coord, y_coord+1) not in visited:
            find_words(results, word_table, word_length, curr_len+1, update_visited, prev_string, (x_coord, y_coord+1), dictionary)
    if x_coord+1 < rows and y_coord+1 < columns:
        if (x_coord+1, y_coord+1) not in visited:
            find_words(results, word_table, word_length, curr_len+1, update_visited, prev_string, (x_coord+1, y_coord+1), dictionary)
    if x_coord+1 < rows:
        if (x_coord+1, y_coord) not in visited:
            find_words(results, word_table, word_length, curr_len+1, update_visited, prev_string, (x_coord+1, y_coord), dictionary)
    if x_coord+1 < rows and y_coord-1 >= 0:
        if (x_coord+1, y_coord-1) not in visited:
            find_words(results, word_table, word_length, curr_len+1, update_visited, prev_string, (x_coord+1, y_coord-1), dictionary)
    if y_coord-1 >= 0:
        if (x_coord, y_coord-1) not in visited:
            find_words(results, word_table, word_length, curr_len+1, update_visited, prev_string, (x_coord, y_coord-1), dictionary)


def get_input(word_length, word_table, rows):
    rows = unicode(raw_input("Please enter the number of rows of letters: "), 'utf-8')
    if rows.isnumeric():
        if not float(rows).is_integer():
            print "Number of rows must be an integer"
            exit()
    else:
        print "Number of rows must be an integer"
        exit()

    word_length = unicode(raw_input("Please enter the number of letters in the word: "), 'utf-8')
    if word_length.isnumeric():
        if not float(word_length).is_integer():
            print "Number of letters must be an integer"
            exit()
    else:
        print "Number of letters must be an integer"
        exit()


    print "\n\n\nYou will now be prompted to input strings of characters representing each row. If there is an empty space in a row, enter '-' in the string.\n For example, if the wordbubbles grid of letters looked like this:\nA B D F\nD A B S\nS N   K\n you would enter 'ABDF' for row 1, 'DABS' for row 2, and 'SN-K' for row 3.\n\n\n"
    for num in range(int(rows)):
        word_table.append(raw_input("Please enter a string of characters representing row #"+str(num)+": "))
    return (int(word_length), int(rows))



#---------------------------------------HANDLE INPUT------------------------------------------
if __name__ == '__main__':

    word_table = []
    results = set([])
    word_length = 0
    rows = 0
    dictionary = enchant.Dict("en_US")

    values = get_input(word_length, word_table, rows)
    word_length = values[0]
    rows = values[1]

    #----------------------------------FIND SOLUTIONS-----------------------------------------

    #Run the function to search for words of the target length at every location.
    for x_coord in range(rows):
        for y_coord in range(len(word_table[0])):
            curr_coord = (x_coord, y_coord)
            visited = set([])
            find_words(results, word_table, word_length, 1, visited, "", curr_coord, dictionary)

    for item in results:
        print item

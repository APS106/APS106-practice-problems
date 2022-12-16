# Write a program that asks a user to enter a string and output letter 
# that appears the most times and the number of times it appears. 
# You need to deal with both capital and lower-case letters.

def max_count_list(s):
    '''
    (str) -> tuple(str, int)
    Return the letter than appears the most times in s together with 
    the number of times it appears
    '''
    # initialize a list to store the number of times each letter appears
    for i in range(26):
        counts.append(0)

    # for each letter, add 1 to the list for that number
    for i in word:
        counts[ord(i) - ord('a')] += 1 # why does this work?

    # find the index of the max entry in a
    index = 0
    for i in range(len(counts)):
        if counts[i] > counts[index]:
            index = i

    return (chr(index+ord('a')), counts[index])

def max_count_dict(s):
    '''
    (str) -> tuple(str, int)
    Return the letter than appears the most times in s together with 
    the number of times it appears
    '''
    counts = {}

    # for each letter, add 1 to the list for that number
    for i in word:
        counts[i] = counts.get(i,0) + 1 # why does this work?

    # find the index of the max entry in a
    max_letter = word[0] # initialize to some letter that we know is in the dictionary
    for i in counts:
        if counts[i] > counts[max_letter]:
            max_letter = i

    return (max_letter, counts[max_letter])

def max_count_dict_one_loop(s):
    '''
    (str) -> tuple(str, int)
    Return the letter than appears the most times in s together with 
    the number of times it appears
    '''
    counts = {}

    max_letter = word[0] # initialize to some letter that we know is in the dictionary

   # for each letter, add 1 to the list for that number
    for i in word:
        counts[i] = counts.get(i,0) + 1 # why does this work?

        if counts[i] > counts[max_letter]:
            max_letter = i

    return (max_letter, counts[max_letter])

word = input("Enter a word: ")
counts = []
word = word.lower()

(letter, num_times) = max_count_list(word)
print("The letter " + letter +"/"+ letter.upper()+ " appears most often: ", num_times, "times." )

(letter, num_times) = max_count_dict(word)
print("The letter " + letter +"/"+ letter.upper()+ " appears most often: ", num_times, "times." )

(letter, num_times) = max_count_dict_one_loop(word)
print("The letter " + letter +"/"+ letter.upper()+ " appears most often: ", num_times, "times." )

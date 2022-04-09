# PartA.py
# Epiphany Chua
# X1095935
# chuaea@uci.edu

# CS 121 Assignment 1: Text Processing
# Part A: Word Frequencies  (40 points)

import sys  # used to read the command line input
import re   # used to parse the file
from operator import itemgetter     # used to access values in dictionary

# function has linear time complexity O(n) due to the while loop
# that reads the entire file into tokens
def tokenize(filepath):
    """
        function that reads in a text file and returns a list of the tokens in that file
        tokens are a sequence of alphanumeric characters, independent of capitalization

        input:
        filepath - path to the textfile

        return:
        tokens - list of tokens (lowercase)
    """
    # open the file from the command line argument
    # checks if file is valid
    try:
        open(filepath, 'r').close()
    
    except IOError:
        print('Trouble opening file')

    file1 = open(filepath, 'r') 
    # instantiate tokens list that will be returned
    tokens = []

    # read in the file line by line
    # while loop total time efficiency: linear
    # O(n + n) = O(2n) => O(n)
    while True:
        line = str(file1.readline())

        # stop loop when end of file is reached
        if not line:
            break

        # use regex findall function to find the tokens in the current line 
        # while filtering the non-alphanumeric chatracters
        # linear time efficiency O(n)
        line_tokens = re.findall(r'[a-zA-Z0-9]+', line)

        # append every token in the line to tokens list
        # make tokens all lowercase
        # linear time efficiency O(n)
        for token in line_tokens:
            tokens.append(token.lower())

    file1.close()

    # return the token list
    return tokens

# function has linear time complexity O(n) due to the for loop that 
# visits every token
def computeWordFrequencies(tokens):
    """
        function that counts the number of occurrences of each token in the token list
        and returns a dictionary with the counts for each token

        input:
        tokens - list of tokens

        return:
        counts - dictionary with token(string):count(int)
    """
    # initialize dictionary
    counts = {}

    # go through every token in the list
    # for loop has linear time efficiency O(n) since dictionaries 
    # have O(1) lookup and insertion properties
    for token in tokens:
        # if token is in dictionary, increment count value
        # O(1) constant time complexity when checking for value in dictionary
        if token in counts:
            counts[token] += 1
        else:
            # if token is not in dictionary, add new token with count = 1
            counts.update({token:1})
    # return counts dictionary
    return counts


# total time efficiency = O(nlogn + nlogn + n) = O(2nlogn + n) => O(nlogn)
# this comes from the use of python's sort() and sorted() method
def printTokenCounts(counts):
    """
        method that prints out the word frequency count onto the screen
        ordered by decreasing frequency and alphabetically)

        input:
        counts - dictionary with token(string):counts(int)

        return:
        prints the token and frequency with the format <token> <freq>
    """

    # first, sort the inputted dictionary by the tokens alphabetically
    # sorted() returns a list of tuples
    # Python's Timsort has O(nlogn) worst case time complexity and O(n) best case
    sortedTokens = (sorted(counts.items(), key = itemgetter(0)))

    # next, sort the list by decreasing frequency
    # sort() uses an in-place algorithm for space efficiency
    # time complexity O(nlogn)
    sortedTokens.sort(reverse=True, key = itemgetter(1))
    
    # print each token and frequency pair
    # linear time efficiency O(n)
    for token, count in sortedTokens:
        print(token, count)


def main():
    """
        when run from the command line, program takes one text file as an argument
        and outputs the token frequencies
    """
    # checks for correct number of arguments from command line
    if not len(sys.argv) == 2:
        raise TypeError('1 argument needed ({len} given)'
                        .format(len = len(sys.argv) - 1))
    # call tokenize function 
    tokens = tokenize(sys.argv[1])

    # call computeWordFrequncies function
    tokencounts = computeWordFrequencies(tokens)

    # call print function
    printTokenCounts(tokencounts)

if __name__ == "__main__":
    main()
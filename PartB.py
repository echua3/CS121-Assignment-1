# PartB.py
# Epiphany Chua
# X1095935
# chuaea@uci.edu

# CS 121 Assignment 1: Text Processing
# Part B: Intersection of two files (60 points)

import PartA
import sys 

# the function's total runtime complexity is linear O(n)
# O(n + n + n + n + n) = O(5n) => O(n)
# this is due to the linear functions from part A and the two for loops
# which checks for intersections and prints out tokens
def intersection(filepath1, filepath2):
    """ 
        function takes two filepaths, reads the files, finds & counts their
        intersecting tokens, and outputs the results

        input:
        filepath1 - path to first textfile
        filepath2 - path to second textfile

        return:
        prints the common words and number of tokens they have in common

    """
    # tokenize first file and put into dictionary
    # use PartA.tokenize and PartA.computeWordFrequencies functions
    # both functions have linear time complexity O(n)
    file1_dict = PartA.computeWordFrequencies(PartA.tokenize(filepath1))

    # instantiate empty set and common token counter
    intersections = set()
    num_common = 0

    # tokenize second file
    # linear time complexity O(n)
    file2_tokens = PartA.tokenize(filepath2)

    # iterate through file2 token list
    # linear time complexity O(n)
    for token in file2_tokens:
        # check if token is in file 1
        if token in file1_dict:

            # check if intersection previously found
            if token not in intersections:
                # add token to intersections set
                intersections.add(token)
                # increment common token counter
                num_common += 1
    
    # print the common tokens
    # linear time complexity O(n)
    for word in intersections:
        print(word)
    print(num_common)
            

def main():
    """
        when run from the command line, program takes two text files 
        from the command line as arguments and outputs the number of 
        tokens they have in common
    """
    intersection(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
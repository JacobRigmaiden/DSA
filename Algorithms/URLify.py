# Write a method to replace all spaces in a string with "%20". You may assume the the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. 

Example:
Input: "MR John Smith", 13
Output: "MR%20John%20Smith"

# in Python, strings are immutable, thus we are forced to implement with lists of single characters
def URLify(string):
    # compute length of new string based on # of spaces in input string
    new_len = 0
    reader = len(string) - 1  # index at end of un-extended string
    for char in string:
        if char == ' ':
            new_len += 3
        else:
            new_len += 1
    # extend length of string to fit URL
    string += [' '] * (new_len - len(string))
    writer = len(string) - 1  # index at end of extended string
    # traverse using double index technique to do this "in place"
    while reader >= 0 and writer >= 0:
        if string[reader] == ' ':  # if reader sees a space, the writer writes %20
            string[writer] = '0'
            string[writer - 1] = '2'
            string[writer - 2] = '%'
            reader -= 1  # reader and writer are advanced accordingly
            writer -= 3
        else:
            string[writer] = string[reader]  # if the reader sees a non-space, the writer copies it over
            reader -= 1  # reader and writer are advanced the same amount
            writer -= 1
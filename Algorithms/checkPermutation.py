
# Clean but less efficient solution is to sort each string and then compare them.

def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    charMap = {}
    for char in string1:
        if char not in charMap:
            charMap[char] = 1
        else:
            charMap[char] += 1
    
    for char in string2:
        if char not in charMap:
            return False

        charMap[char] -= 1
        if charMap[char] < 0:
            return False
    
    return True


# Notes: if no neg char in charMap then no positive values either because of the direct pos/neg char relationship between the two strings
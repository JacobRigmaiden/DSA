



def isUnique(phrase):
    charMap = {}
    for char in phrase:
        if char not in charMap:
            charMap[char] = 1
        else:
            return False
    return True


# Notes:
# Ask if the phrase contains ASCII or just unicode: If it does contain ASCII then we would need to increase the memory of the algo if you use JAva or such. 256 is ASCII unique values
# In the case of pure alphabet, you can check if phrase length exceeds 128 (lower and upper case counts) if it does then you can return false
# If I cannot use additional data structures then I would have to brute force it and the runtime would be O(n^2)

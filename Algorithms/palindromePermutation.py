# Given a string, check if it is a permutation of a palindrome.

def palindromePermutation(input):
    charMap = {}
    for char in input:
        if char == " ":
            continue
        if char not in charMap:
            charMap[char] = 1
        else:
            charMap[char] += 1
    oddCount = 0
    for char in charMap:
        if charMap[char] & 1:
            oddCount += 1
    print(oddCount)
    if oddCount == 1 or oddCount == 0:
        print("true")
        return True

    print("returning false")
    return False


x = "taoc tc"
palindromePermutation(x)
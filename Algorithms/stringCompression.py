# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller
# thatn the original string, your method should return the original string. You can assume the string has only
# 1 uppercase and lowercase letters (a-z).

def stringCompression(string):
    compressedString = []
    current = string[0]
    counter = 1
    
    for char in string[1:]:
        if char == current:
            counter += 1
        else:
            compressedString.append(char + str(counter))
    compressedString.append(char + str(counter))
    compressedString = "".join(compressedString)

    if len(compressedString) > len(string):
        return string
    else:
        return compressedString            
    
x = "aabcccccaaa"
z = stringCompression(x)
print(z)
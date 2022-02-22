# There are three types of edits that can be performed on string: insert a char, remove a char, or replace a char. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def oneEditAway(first, second):
    if len(first) == len(second):
        return oneEditReplace(first, second)
    elif len(first) + 1 == len(second):
        return oneEditInsert(first, second)
    elif len(first) - 1 == len(second):
        return oneEditInsert(second, first)
    else:
        return False
    

def oneEditReplace(first, second):
    diffFound = False
    for i, val in enumerate(first):
        if val != second[i]:
            if diffFound:
                return False
            
            diffFound == True
    return True

def oneEditInsert(first, second):
    index1 = 0
    index2 = 0

    while index2 < len(second) and index1 < len(first):
        if first[index1] != second[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index2 += 1
            index1 += 1
    return True


x = "car"
y = "cars"
z = oneEditAway(x, y)
print(z)
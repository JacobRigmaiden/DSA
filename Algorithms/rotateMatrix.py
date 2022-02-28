# Given an image represented by an NxN matrix, where each pixel in the image is representedby an integer,
# write a method to rotate the image by 90 degrees. Can you do this in place?

# Pseudo:
# for i = 0 to n
#     temp = top[1]
#     top[i] = left[i]
#     left[i] = bottom[i]
#     bottom[i] = right[i]
#     right[i] = temp


def rotateMatrix(matrix):
    if len(matrix) != len(matrix[0]) or len(matrix) == 0:
        return False
    
    n = len(matrix)
    for layer in range(int(n / 2)):
        first = layer
        last = n - 1 - layer
        for i in range(last):
            offset = i - first
            # Save top temporarily so we can insert it at the end
            top = matrix[first][i]
            
            matrix[first][i] = matrix[last - offset][first]
            
            matrix[last - offset][first] = matrix[last][last - offset]
            
            matrix[last][last - offset] = matrix[i][last]
            
            matrix[i][last] = top
    return matrix


input = [[1,2,3],[4,5,6],[7,8,9]]
x = rotateMatrix()
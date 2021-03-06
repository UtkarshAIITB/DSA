# link : https://leetcode.com/problems/rotate-image/

# the basic observation is:
# before rotation = x,y 
# after rotation = X, Y
# X = y
# Y = n-x
# n = size of matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(len(matrix))

n = len(matrix)
for i in range(n // 2 + n % 2):
    for j in range(n // 2):
        tmp = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
        matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
        matrix[j][n - 1 - i] = matrix[i][j]
        matrix[i][j] = tmp


# print(matrix)
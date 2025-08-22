def rotate_matrix(matrix):

    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            print(matrix[i][j])
            print(matrix[j][i])
            matrix[i][j] , matrix[j][i] = matrix[j][i],matrix[i][j]
    for row in matrix:
        row[:] = row[::-1]
    
list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

rotate_matrix(list)
print(list)
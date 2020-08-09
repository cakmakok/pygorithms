def zero_matrix(matrix):
    zero_coordinates = []
    for r_idx, row in enumerate(matrix):
        for c_idx, item in enumerate(row):
            if item == 0:
                zero_coordinates.append((r_idx,c_idx))

    for coordinate in zero_coordinates:
        for i in range(0,len(matrix)):
            matrix[coordinate[0]][i] = 0
            matrix[i][coordinate[0]] = 0

    print(zero_coordinates)

test_matrix = [[1, 2, 3],
               [4, 0, 6],
               [7, 8, 0]]

zero_matrix(test_matrix)
print(test_matrix)

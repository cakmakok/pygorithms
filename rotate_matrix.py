def rotate_matrix(matrix):
    num_of_layers =  len(matrix)//2
    matrix_length = len(matrix)
    for layer in range(0, num_of_layers):
        start_idx = layer
        end_idx = matrix_length -layer-1
        for i in range(start_idx, end_idx):
            tmp = matrix[layer][i]
            matrix[layer][i] = matrix[matrix_length-i-1][layer]
            matrix[matrix_length - i - 1][layer] = matrix[matrix_length-layer-1][matrix_length-i-1]
            matrix[matrix_length-layer-1][matrix_length-i-1] = matrix[i][matrix_length-layer-1]
            matrix[i][matrix_length - layer - 1]  = tmp
    

test_matrix = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

rotate_matrix(test_matrix)
print(test_matrix)

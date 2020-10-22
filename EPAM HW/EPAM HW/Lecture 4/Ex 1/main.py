def transpose_a_matrix(MATRIX: list) -> list:
    T_MATRIX = []
    for i in range(len(MATRIX[0])):
        T_MATRIX.append([])
        for j in range(len(MATRIX)):
            T_MATRIX[i].append(MATRIX[j][i])
    return T_MATRIX


def output_matrix(MATRIX: list) -> None:
    for elem in MATRIX:
        print(elem)

s
if __name__ == '__main__':
    # MATRIX = [[0, 1, 2], [3, 4, 5]]
    MATRIX = [[0, 1, 9], [9, 8, 5], [7, 3, 1], [3, 4, 0]]
    print('Original matrix is:')
    output_matrix(MATRIX)
    print('\nTransposed matrix is:')
    output_matrix(transpose_a_matrix(MATRIX))

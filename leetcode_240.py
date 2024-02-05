def solve(matrix, target):
    row, col = len(matrix), len(matrix[0])

    val = matrix[0][col - 1]

    i, j = 0, col - 1
    while i < row and j >= 0:
        if val > target:
            j -= 1
        elif val < target:
            i += 1
        else:
            return True

        val = matrix[i][j]

    return False


print(solve([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parentheses(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parentheses(s, i, s[i][j])
        print_optimal_parentheses(s, s[i][j] + 1, j)
        print(")", end="")


# Example usage
matrix_dims = [3, 3, 4, 2, 2, 3]
m, s = matrix_chain_order(matrix_dims)
print("Minimum number of multiplications:", m[1][len(matrix_dims) - 1])
print("Optimal parenthesization:", end=" ")
print_optimal_parentheses(s, 1, len(matrix_dims) - 1)

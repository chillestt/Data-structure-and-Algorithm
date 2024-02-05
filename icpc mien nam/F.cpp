#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const long long MOD = 998244353;

vector<vector<long long>> matrix_multiply(vector<vector<long long>>& A, vector<vector<long long>>& B) {
    vector<vector<long long>> result(2, vector<long long>(2, 0));
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                result[i][j] += (A[i][k] * B[k][j]);
                //result[i][j] %= MOD;
            }
        }
    }
    return result;
}

void printMatrix(const std::vector<std::vector<long long>>& matrix) {
    for (size_t i = 0; i < matrix.size(); i++) {
        for (size_t j = 0; j < matrix[i].size(); j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}


vector<vector<long long>> matrix_power(vector<vector<long long>>& matrix, int n) {
    vector<vector<long long>> result(2, vector<long long>(2, 0));
    result[0][0] = result[1][1] = 1;
    while (n > 0) {
        if (n % 2 == 1) {
            result = matrix_multiply(result, matrix);
        }
        matrix = matrix_multiply(matrix, matrix);
        n /= 2;
    }
    return result;
}

long long fibonacci_power_sum(int n, int k) {
    long long sum_powers = 0;
    if (n < 1) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }

    for (int i = 1; i <= n; i++) {
        vector<vector<long long>> matrix(2, vector<long long>(2, 0));
        matrix[0][0] = matrix[0][1] = matrix[1][0] = 1;
        vector<vector<long long>> matrix_to_power_n_minus_1 = matrix_power(matrix, i - 1);
        //printMatrix(matrix_to_power_n_minus_1);
        sum_powers = (sum_powers + (long) pow(matrix_to_power_n_minus_1[0][0], k) % MOD);
    }

    return sum_powers;
}

int main() {
    int n, k;
    cin >> n >> k;
    long long result = fibonacci_power_sum(n, k);
    cout << result << endl;
    return 0;
}

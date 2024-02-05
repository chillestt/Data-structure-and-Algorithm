import math


def H(a, b, c, d):
    factors = []

    for i in range(1, int(math.sqrt(c)) + 1):
        if c % i == 0:
            factors.append(i)
            if c / i != i:
                factors.append(int(c / i))

    factors = sorted(factors)

    ans = -1
    for i in range(0, len(factors)):
        factor = factors[i]
        if factor % a == 0 and factor % b != 0 and d % factor != 0:
            ans = factor
            break

    return ans


a, b, c, d = list(map(int, input().split()))
print(H(a, b, c, d))

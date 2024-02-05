def find_smallest_K(M):
    if M == 0:
        return 10
    if M == 1:
        return 1

    factors = []

    for i in range(9, 1, -1):
        while M % i == 0:
            factors.append(i)
            M //= i

    if M > 1:
        return -1

    ans = 0
    pw = 0
    for i in factors:
        ans += i * 10**(pw)
        pw += 1
    return ans


n = int(input())
print(find_smallest_K(n))
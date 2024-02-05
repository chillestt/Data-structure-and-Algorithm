from itertools import combinations

def gcd(m,n):
    if m< n:
        (m,n) = (n,m)
    while (m % n != 0):
        (m, n) = (n, m % n)
    return n


def C(arr):
    n = len(arr)
    total_gcd = sum(arr)

    for r in range(2, n + 1):
        for subset in combinations(arr, r):
            # Calculate the GCD of the subset's elements and add it to the total
            subset_gcd = total_gcd
            for num in subset:
                subset_gcd = gcd(subset_gcd, num)
            total_gcd += subset_gcd

    return total_gcd % (10**9 + 7)


n = int(input())
for i in range(n):
    l = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    print(C(arr))

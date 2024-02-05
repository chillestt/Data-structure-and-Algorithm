def sum_of_divisors(n):
    result = 1  # Initialize with 1 for the prime factor 1
    p = 2  # Start with the smallest prime factor

    while p * p <= n:
        if n % p == 0:
            j = p * p
            n //= p
            while n % p == 0:
                j *= p
                n //= p
            result *= (j - 1) // (p - 1)

        if p == 2:
            p = 3
        else:
            p += 2

    if n > 1:
        result *= (n + 1)

    return result


n = int(input())
print(f(n))

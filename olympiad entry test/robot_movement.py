
def minimum_battery(inputs):
    min_height = float("inf")
    c = 0

    for h in inputs:
        c = max(c, h - min_height)
        min_height = min(h, min_height)

    return c


n = int(input())
a = [list(map(int, input().strip().split()))[-1] for _ in range(n)]
print(minimum_battery(a))

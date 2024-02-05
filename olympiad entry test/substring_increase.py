n = int(input())
arr = list(map(int, input().strip().split()))


def find_max_length(n, nums):
    cur_length = 0
    max_length = 0

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            cur_length += 1
        else:
            max_length = max(max_length, cur_length)
            cur_length = 1

    return max(max_length, cur_length)


print(find_max_length(n, arr))

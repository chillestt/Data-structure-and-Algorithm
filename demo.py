def solution(intervals):
    n = len(intervals)
    sorted_intervals = sorted([(interval[0], i) for i, interval in enumerate(intervals)])
    res = [-1] * n
    for i in range(n):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_intervals[mid][0] >= intervals[i][1]:
                res[i] = sorted_intervals[mid][1]
                break
            elif sorted_intervals[mid][0] < intervals[i][1]:
                left = mid + 1
        if left > right:
            res[i] = -1
    return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solution(intervals))

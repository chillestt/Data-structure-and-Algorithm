
def recSearch(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return recSearch(arr, l + 1, r - 1, x)


def binary_search(arr, l, r, x):
    if r < l:
        return -1
    mid = l + (r - l) // 2
    if arr[mid] > x:
        return binary_search(arr, l, r - 1, x)
    elif arr[mid] < x:
        return binary_search(arr, l + 1, r, x)
    else:
        return mid


if __name__ == "__main__":
    arr = [1, 4, 5, 7, 9, 0]
    idx = binary_search(arr, 0, len(arr) - 1, 0)
    print(f"finding element is at the index {idx}")

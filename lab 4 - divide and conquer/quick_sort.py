def hoarePartition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i+=1

        j-=1
        while arr[j] > pivot:
            j-=1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high:
        pi = hoarePartition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    arr = [9, 90, 36, 7, 89]
    quick_sort(arr, 0, 4)
    print(arr)

# https://classroom.codingninjas.com/app/classroom/me/14074/content/257232/offering/3505428/problem/1138

# Quick Sort Code

# Sort an array A using Quick Sort.
# Change in the input array itself. So no need to return or print anything.


def quickSort(arr: list, start: int, end: int) -> None:
    if start >= end:
        return

    count = 0
    for i in range(start + 1, end + 1):
        if arr[start] > arr[i]:
            count += 1

    pivot = start + count
    arr[start], arr[pivot] = arr[pivot], arr[start]

    i = start
    j = end

    while (i < pivot) and (pivot < j):
        if arr[i] < arr[pivot]:
            i += 1

        if arr[j] >= arr[pivot]:
            j -= 1

        if arr[i] >= arr[pivot] and arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quickSort(arr, start, pivot - 1)
    quickSort(arr, pivot + 1, end)


n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
quickSort(arr, 0, n - 1)
print(*arr)

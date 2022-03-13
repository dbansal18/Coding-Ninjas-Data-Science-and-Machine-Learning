# https://classroom.codingninjas.com/app/classroom/me/14074/content/257232/offering/3505425/problem/44

# Merge Sort Code

# Sort an array A using Merge Sort.
# Change in the input array itself. So no need to return or print anything.


def merge(a1, a2, a):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            k = k + 1
            i = i + 1
        else:
            a[k] = a2[j]
            k = k + 1
            j = j + 1
    while i < len(a1):
        a[k] = a1[i]
        k = k + 1
        i = i + 1
    while j < len(a2):
        a[k] = a2[j]
        k = k + 1
        j = j + 1


def merge_sort(a):
    if len(a) == 0 or len(a) == 1:
        return
    mid = len(a) // 2
    a1 = a[0:mid]
    a2 = a[mid:]

    merge_sort(a1)
    merge_sort(a2)
    merge(a1, a2, a)


def mergeSort(arr: list, start: int, end: int) -> None:
    merge_sort(arr)


n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
mergeSort(arr, 0, n)
print(*arr)

# https://classroom.codingninjas.com/app/classroom/me/14075/content/257278/offering/3506139/problem/389

# Spiral Print

# For a given two-dimensional integer array/list of size (N x M), print it in a spiral form.
# That is, you need to print in the order followed for every iteration:
# a. First row(left to right)
# b. Last column(top to bottom)
# c. Last row(right to left)
# d. First column(bottom to top)
#  Mind that every element will be printed only once.


from sys import stdin


def spiralPrint(a: list, m: int, n: int) -> None:
    k = 0
    l = 0

    """ k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator """

    while k < m and l < n:

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")

        n -= 1

        # Print the last row from
        # the remaining rows
        if k < m:

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")

            m -= 1

        # Print the first column from
        # the remaining columns
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")

            l += 1


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1

# Stock Span

# Afzal has been working with an organization called 'Money Traders' for the past few years.
# The organization is into the money trading business. His manager assigned him a task.
# For a given array/list of stock's prices for N days, find the stock's span for each day.
# The span of the stock's price today is defined as the maximum number of consecutive
# days(starting from today and going backwards) for which the price of the stock was less than today's price.
# For example, if the price of a stock over a period of 7 days are [100, 80, 60, 70, 60, 75, 85],
# then the stock spans will be [1, 1, 1, 2, 1, 4, 6].
# Explanation:
# On the sixth day when the price of the stock was 75, the span came out to be 4, because the last
# 4 prices(including the current price of 75) were less than the current or the sixth day's price.

# Similarly, we can deduce the remaining results.


from sys import stdin


def stockSpan(price: list, n: int) -> list:
    stack = list()
    spans = list()

    for i in range(n):
        if stack:
            while stack and (price[stack[-1]] < price[i]):
                stack.pop()
            if stack:
                spans.append(i - stack[-1])
            else:
                spans.append(i + 1)
        else:
            spans.append(i + 1)
        stack.append(i)

    return spans


"""-------------- Utility Functions --------------"""


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()


def takeInput():
    size = int(stdin.readline().strip())

    if size == 0:
        return list(), 0

    price = list(map(int, stdin.readline().strip().split(" ")))

    return price, size


# main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)

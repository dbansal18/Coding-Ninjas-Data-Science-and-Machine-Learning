# https://classroom.codingninjas.com/app/classroom/me/14074/content/257244/offering/3505611/problem/390

# Check redundant brackets

# For a given expression in the form of a string, find if there exist any redundant brackets or not. It is
# given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.
# A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.
# Example:
# Expression: (a+b)+c
# Since there are no needless brackets, hence, the output must be 'false'.

# Expression: ((a+b))
# The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.


from sys import stdin


def checkRedundantBrackets(expression: str) -> bool:
    stack = list()

    for ele in expression:
        if ele == ")":
            count = 0
            while stack.pop() != "(":
                count += 1
            if count < 2:
                return True
        else:
            stack.append(ele)

    return False


# main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression):
    print("true")

else:
    print("false")

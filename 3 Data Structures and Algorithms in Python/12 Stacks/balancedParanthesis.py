# https://classroom.codingninjas.com/app/classroom/me/14074/content/257244/offering/3505605/problem/418

# Balanced Paranthesis

# For a given a string expression containing only round brackets or parentheses, check if they are balanced or not.
# Brackets are said to be balanced if the bracket which opens last, closes first.
# Example:
# Expression: (()())
# Since all the opening brackets have their corresponding closing brackets, we say it is balanced and
# hence the output will be, 'true'.
# You need to return a boolean value indicating whether the expression is balanced or not.


from sys import stdin


class Stack:
    def __init__(self):
        self.list = []
        self.size = 0

    def empty(self):
        return self.size == 0

    def top(self):
        if self.empty():
            return "Stack is empty"
        return self.list[self.size - 1]

    def push(self, ele):
        self.list.append(ele)
        self.size += 1

    def pop(self):
        if self.empty():
            return "Stack is empty"
        self.size -= 1
        return self.list.pop()


def isBalancedAlternative(exp):
    # Your code goes here
    stack = []
    for char in exp:
        if char in ["("]:
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    if not stack:
        return True
    else:
        return False


def isBalanced(exp):
    i = 0
    for ele in exp:
        if ele == "(":
            i += 1
        else:
            i -= 1
            if 0 > i:
                return False
    return i == 0


# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")

else:
    print("false")

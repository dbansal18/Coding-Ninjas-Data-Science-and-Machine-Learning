# https://classroom.codingninjas.com/app/classroom/me/14075/content/257268/offering/3505989/problem/3096

# Calculator
# Write a program that performs the tasks of a simple calculator.
# The program should first take an integer as input and then based on that integer perform the task as given below.

while 1:
    op = int(input())

    if op == 1:
        a = int(input())
        b = int(input())
        print(a + b)
    elif op == 2:
        a = int(input())
        b = int(input())
        print(a - b)
    elif op == 3:
        a = int(input())
        b = int(input())
        print(a * b)
    elif op == 4:
        a = int(input())
        b = int(input())
        print(a // b)
    elif op == 5:
        a = int(input())
        b = int(input())
        print(a % b)
    elif op == 6:
        break
    else:
        print("Invalid Operation")

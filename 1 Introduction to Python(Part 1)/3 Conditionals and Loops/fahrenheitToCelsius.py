# https://classroom.codingninjas.com/app/classroom/me/14075/content/257268/offering/3505987/problem/966

# Fahrenheit to Celsius
# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),you need to convert
# all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

s = int(input())
e = int(input())
w = int(input())

while s <= e:
    c = int(((s - 32) * 5) / 9)
    print(s, "\t", c)

    s += w

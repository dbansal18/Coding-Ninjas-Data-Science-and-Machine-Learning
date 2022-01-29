# https://classroom.codingninjas.com/app/classroom/me/14075/content/257272/offering/3506050/problem/1038

# Fahrenheit to Celsius Function

# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
# Input Format :
# 3 integers - S, E and W respectively
# Output Format :
# Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value. Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")


def printTable(s, e, w):
    while s <= e:
        c = int(((s - 32) * 5) / 9)
        print(s, "\t", c)
        s += w


s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)

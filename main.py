# Project Euler
# Problem 1
# import numpy
# from bs4 import BeautifulSoup


def problem1(x):
    result = 0
    for i in range(3, x):
        if i % 3 == 0 or i % 5 == 0:
            assert isinstance(i, int)
            result += i
    return result


def problem2():
    fib = [1]
    i = 2
    x = 2
    result: int = 0

    while x < 4000000:
        fib.append(x)
        x = fib[i - 2] + fib[i - 1]
        i += 1

    for i in fib:
        if 0 == i % 2:
            result += i

    return result


# a = int(input("Please enter integer value - "))
print(problem1(10))

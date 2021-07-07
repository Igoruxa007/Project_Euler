# Project Euler
# Problem 1


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
    result = 0

    while x < 4000000:
        fib.append(x)
        x = fib[i - 2] + fib[i - 1]
        i += 1

    for i in fib:
        if (i % 2 == 0):
            result += i

    print(result)


# a = int(input("Please enter integer value - "))
print(problem2())

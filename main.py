# Project Euler
import math
import time


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


def problem3():
    num = 600851475143

    lst = [2]
    x = []
    start_time = time.process_time()

    for i in range(3, int((math.sqrt(num)) + 1), 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j > int((math.sqrt(i)) + 1):
                lst.append(i)
                if num % i == 0:
                    x.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)

    print(time.process_time() - start_time)
    print(lst)
    print(x)


def problem48():
    start_time = time.process_time()
    x = 0
    for i in range(1, 1001):
        x += i ** i
    print(time.process_time() - start_time)
    return str(x)[-10:]


def spin_words(sentence):
    s1 = []
    for x in sentence.split(" "):
        if len(x) >= 5:
            s1.append(x[::-1])
        else:
            s1.append(x)
    return " ".join(s1)


# a = int(input("Please enter integer value - "))
print(spin_words("Your sentence"))

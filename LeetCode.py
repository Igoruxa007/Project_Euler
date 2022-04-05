import sys


def roman_to_integer(s):
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s.replace("\"", "")
    converted_digits = list()
    for char in s:
        converted_digits.append(dictionary[char])
    integer = converted_digits[len(converted_digits) - 1]
    for i in reversed(range(len(converted_digits) - 1)):
        if converted_digits[i + 1] > converted_digits[i]:
            integer -= converted_digits[i]
        else:
            integer += converted_digits[i]
    return integer


def exercise():
    with open('input.txt', 'r') as file_to_read:
        numbers = file_to_read.read().split(" ")
        with open('output.txt', 'w') as file_to_write:
            file_to_write.write(str(int(numbers[0]) + int(numbers[1])))


def exercise3(num):
    return int(num[0]) + int(num[1])


try:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(' ', range(c, d+1), sep="\t")
    for i in range(a, b+1):
        x = [str(i)]
        for j in range(c, d + 1):
            x.append(str(i*j))
        line = '\t'.join(x)
        print(line)
except:
    pass

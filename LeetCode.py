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


# чтение из потока двух цифр и вывод их суммы
str_in = sys.stdin.readlines()
numbers = str_in[0].split(" ")
string = str(int(numbers[0]) + int(numbers[1]))
sys.stdout.write(string)
# print(exercise3(numbers))

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

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1:
             if flowerbed[0] == 0:
                return 1 == n
             elif flowerbed[0] == 1:
                return 0 == n
        counter = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                counter += 1
        for i  in range(1, len(flowerbed)-2):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                counter += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                counter += 1
        return counter == n


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPlaceFlowers([0], 1))

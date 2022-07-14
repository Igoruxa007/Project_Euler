import math
import re
from typing import Dict


def pig_it(text):
    new_words = list()
    numbers = text.split(" ")
    for words in numbers:
        if words.isalpha():
            new_words.append(words[1:len(words)] + words[0] + 'ay')
        else:
            new_words.append(words)
    return ' '.join(new_words)


def smh_to_str(smh):  # ______________________________Human Readable Time
    if len(str(smh)) == 1:
        return "0" + str(smh)
    else:
        return str(smh)


def make_readable(seconds):
    num = list()
    num.append(seconds // 3600)
    num.append((seconds // 60) % 60)
    num.append(seconds % 60)
    for i in range(len(num)):
        num[i] = smh_to_str(num[i])
    return ":".join(num)


def make_readable_best(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)


def square_sum(numbers):  # _____________________________Square(n) Sum
    sum_of_num = 0
    for num in numbers:
        sum_of_num += num * num
    return sum_of_num


def is_isogram(string):
    """Isogram

    """
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


def create_phone_number(n):  # _______________________________ Create phone number
    number = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    return number


def likes(names):  # __________________________________________ Who like this
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(**names[:3], others=n - 2)


def roman_numerals_encoder(n):  # _________________________ Roman Numerals Encoder
    units = {
        0: '',
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX'
    }[n % 10]
    ten = {
        0: '',
        1: 'X',
        2: 'XX',
        3: 'XXX',
        4: 'XL',
        5: 'L',
        6: 'LX',
        7: 'LXX',
        8: 'LXXX',
        9: 'XC'
    }[n % 100 // 10]
    hundred = {
        0: '',
        1: 'C',
        2: 'CC',
        3: 'CCC',
        4: 'CD',
        5: 'D',
        6: 'DC',
        7: 'DCC',
        8: 'DCCC',
        9: 'CM'
    }[n % 1000 // 100]
    over = (n // 1000) * 'M'
    return over + hundred + ten + units


def roman_numerals_encoder_solution(n):
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                      }
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string


def find_odd(seq):
    """Find the odd int

    """
    odd_dict = {}
    for number in seq:
        if number in odd_dict:
            odd_dict[number] = odd_dict[number] + 1
        else:
            odd_dict[number] = 1

    for element in sorted(odd_dict.keys()):
        if odd_dict[element] % 2 == 1:
            return element


def persistence(n):
    """Persistent Bugger
    Function that takes in a positive parameter num and returns its multiplicative persistence,
    which is the number of times you must multiply the digits in num until you reach a single digit.
    """

    if n < 10:
        return 0
    else:
        new_numeric = math.prod([int(a) for a in str(n)])
        return persistence(new_numeric) + 1


def find_unique(arr):
    """Find the unique number

    """
    if arr[0] != arr[1]:
        if arr[0] == arr[2]:
            return arr[1]
        else:
            return arr[0]
    else:
        equal_number = arr[0]
    for number in arr:
        if number != equal_number:
            return number


def high(x):
    """Highest Scoring Word

    """
    price_of_words = list()
    words = x.split()
    for word in words:
        x = 0
        for letter in word:
            x += ord(letter) - 96
        price_of_words.append(x)
    return words[price_of_words.index(max(price_of_words))]


def comp(array1, array2):
    """Are they the "same"
    Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays
    have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times
    it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

    For this kata added two array a1 and a2 before print
    """

    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


def dig_pow(a1, a2):
    """Playing with digits

    """
    num_as_str = str(a1)
    sum_of_number = sum([int(num_as_str[i]) ** (a2 + i) for i in range(len(num_as_str))])
    return a1 // sum_of_number if a1 % sum_of_number == 0 else -1


def beeramid(bonus, price):
    """Beeramid
    A beer can pyramid will square the number of cans in each level - 1 can in the top level,
    4 in the second, 9 in the next, 16, 25...
    """
    num_of_can = bonus / price
    can_in_pyramid = 0
    for i in range(1, 100):
        can_in_pyramid += i ** 2
        if num_of_can < can_in_pyramid:
            return i - 1


def snail(snail_map):
    """Snail Sort

    """
    x = list()
    for i in range(0, len(snail_map) // 2):
        for j in range(i, len(snail_map) - i):
            x.append(snail_map[i][j])
        for j in range(i + 1, len(snail_map) - i - 1):
            x.append(snail_map[j][-(i + 1)])
        for j in range(len(snail_map) - i - 1, i - 1, -1):
            x.append(snail_map[-i - 1][j])
        for j in range(len(snail_map) - i - 2, i, -1):
            x.append(snail_map[j][i])
    if len(snail_map) % 2 > 0:
        try:
            x.append(snail_map[len(snail_map) // 2][len(snail_map) // 2])
        except:
            pass
    return x


def score(dice):
    x = 0
    for i in range(2, 7):
        if dice.count(i) >= 3:
            x += i * 100
    if dice.count(1) >= 3:
        x += 1000
        x += (dice.count(1) - 3) * 100
    elif dice.count(1) < 3:
        x += dice.count(1) * 100
    if dice.count(5) > 3:
        x += (dice.count(5) - 3) * 50
    elif dice.count(5) < 3:
        x += dice.count(5) * 50
    return x


def solution(string):
    return "".join([x for x in reversed(string)])


def filter_list(list1):
    return [x for x in list1 if isinstance(x, (int, float))]


def same_structure_as(original, other):
    """
    Function to return True when its argument is an array that has the same nesting structures and same
    corresponding length of nested arrays as the first array.
    """
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        return True
    else:
        return isinstance(original, list) and isinstance(other, list)


def number_int_to_str(number):
    units = {0: '',
             1: 'one',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine'}
    t = {10: 'ten',
         11: 'eleven',
         12: 'twelve',
         13: 'thirteen',
         14: 'fourteen',
         15: 'fifteen',
         16: 'sixteen',
         17: 'seventeen',
         18: 'eighteen',
         19: 'nineteen'}
    dozens = {0: '',
              1: '',
              2: 'twenty ',
              3: 'thirty ',
              4: 'forty ',
              5: 'fifty ',
              6: 'sixty',
              7: 'seventy',
              8: 'eighty',
              9: 'ninety'}
    hundreds = {0: '',
                1: 'one hundred ',
                2: 'two hundred ',
                3: 'three hundred ',
                4: 'four hundred ',
                5: 'five hundred ',
                6: 'six hundred ',
                7: 'seven hundred ',
                8: 'eight hundred ',
                9: 'nine hundred '}
    number_in_str = hundreds[number // 100]
    if number % 100 > 19:
        number_in_str += dozens[number % 100 // 10]
        number_in_str += units[number % 10]
    elif number % 100 > 9:
        number_in_str += t[number % 100]
    elif number == 0:
        number_in_str = 'zero'
    else:
        number_in_str += units[number % 10]
    print(number_in_str)
    return number_in_str


def pig_it(text) -> str:
    new_text = text.split()
    for i in range(len(new_text)):
        if new_text[i].isalpha():
            new_text[i]=new_text[i][1:]+new_text[i][0]+'ay'
    return ' '.join(new_text)


def printer_error(s):
    alphabet = 'abcdefghijklm'
    print(str(sum(map(lambda x: x in alphabet, s))) + '/' + str(len(s)))


def main():
    printer_error("asdfasdfasdf")


if __name__ == '__main__':
    main()

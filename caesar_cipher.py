import string
import math


def moving_shift(s, shift):
    new_s = ""
    result = []

    for letter in s:
        if letter.isupper():
            new_s += string.ascii_uppercase[(string.ascii_uppercase.find(letter) + shift) % 26]
            shift += 1
        elif letter.islower():
            new_s += string.ascii_lowercase[(string.ascii_lowercase.find(letter) + shift) % 26]
            shift += 1
        else:
            new_s += letter
            shift += 1
    k = math.ceil(len(new_s)/5)
    for i in range(1, 6):
        result.append(new_s[(i-1)*k:i*k])

    return result


def demoving_shift(s, shift):
    result = ''.join(s)
    new_s = ""
    for letter in result:
        if letter.isupper():
            new_s += string.ascii_uppercase[(string.ascii_uppercase.find(letter) - shift) % 26]
            shift += 1
        elif letter.islower():
            new_s += string.ascii_lowercase[(string.ascii_lowercase.find(letter) - shift) % 26]
            shift += 1
        else:
            new_s += letter
            shift += 1
    return new_s


print(moving_shift("aux frontizres de la folie le cerveau dzploie ses facultzs tatouages ztranges zme daltonienne ironie du przsent", 1))
x = 'bwa kxvvcskdrg tv eu bl', 'jhe nh hkydnkf qnebfax ', 'nap eadwoxey bjdzgnuti ', 'rmlvjdcr aoh igsbxxtqab', 't zjhhda bt qtcwjta'
print(demoving_shift(x, 1))

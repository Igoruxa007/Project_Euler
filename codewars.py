def pig_it(text):
    new_words = list()
    numbers = text.split(" ")
    for words in numbers:
        if words.isalpha():
            new_words.append(words[1:len(words)] + words[0] + 'ay')
        else:
            new_words.append(words)
    return ' '.join(new_words)


def zero(f=None): return 0 if not f else f(0)


def one(f=None): return 1 if not f else f(1)


def two(f=None): return 2 if not f else f(2)


def three(f=None): return 3 if not f else f(3)


def four(f=None):
    if not f:
        return 4
    else:
        f(4)


def five(f=None): return 5 if not f else f(5)


def six(f=None): return 6 if not f else f(6)


def seven(f=None):
    if not f:
        return 7
    else:
        f(7)


def eight(f=None): return 8 if not f else f(8)


def nine(f=None): return 9 if not f else f(9)


def plus(y): return lambda x: x + y


def minus(y): return lambda x: x - y


def times(y): return lambda x: x * y


def divided_by(y): return lambda x: x / y


# _____________________________________________________________Human Readable Time
def smh_to_str(smh):
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


# _____________________________________________________________Square(n) Sum
def square_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num * num
    return sum


#_____________________________________________________________ Isogram
def is_isogram(string):
    string = string.lower()
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
                break
    return True


print(is_isogram("Dermatoglyphics"))

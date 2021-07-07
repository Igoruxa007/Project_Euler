#Project Euler
#Problem 1

def problem1(x):
    result = 0
    for i in range(3, x):
        if i%3 == 0 or i%5 == 0:
             assert isinstance(i, int)
             result += i
    return result

a = int (input("Please enter integer value - "))
print(problem1(a))

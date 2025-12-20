def virazenie(x):

    def sum(a, b):
        return a + b

    def min(a, b):
        return a - b

    def min1(a, b, c):
        return a * (b - c)

    def sum2(a, b, c):
        return a * (b + c)

    def func(a, b):
        return a - b

    def min2(a, b):
        return a - b

    result1 = sum(2, 1)
    result2 = min(2, 1)
    result3 = min1(3, 2, 1)
    result4 = sum2(7, 2, 1)
    result6 = min2(1, 4)

    z = 8

    division = result1 / result2
    division1 = result3 / result4
    result5 = division - division1
    division2 = z / result6
    result7 = result5 + division2

    print("virazenie = ", result7)

    return result7

virazenie(0)
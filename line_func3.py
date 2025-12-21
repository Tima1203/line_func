def virazenie_v(y):

    def umn(a, b):
        return a * b

    def delen(a, b):
        return a / b

    def vich(a, b):
        return a - b
    
    def sum(a, b): 
        return a + b
    part1_1 = vich(umn(2, y), 1)
    part1_2 = umn(7, y)
    part3_1 = sum(umn(2, y), 1)
    num2 = 8
    num3 = 3
    num4 = sum(umn(2, y), 1)
    num6 = umn(2,y)
    num7 = umn(3,y)

    res1 = delen(part1_1, umn(part1_2, part3_1))
    res2 = delen(num2, vich(umn(num6*num6, num3),num3))
    res3 = delen(part3_1, vich(umn(num6, num7), num7))

    result_v = sum(res1, res2)
    result_v = vich(result_v, res3)

    print("virazenie_v = ", result_v)

    return result_v

virazenie_v(2)


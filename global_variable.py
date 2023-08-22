def add(number1, number2):
    global test
    test = 11
    res = number1 + number2
    print(res)
    return res

test = 10
print(add(1, 2))
print(test)
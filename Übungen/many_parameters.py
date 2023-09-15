def multi(number1, number2, *numbers):
    sum = number1 + number2
    for i in numbers:
        sum += i
    return sum


print(multi(2, 2, 2))

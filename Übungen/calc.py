PI = 3.141592653589793
print(PI)


def addition(a, b):
    return a + b


def facutlty(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


if __name__ == "__main__":
    print("Hello from calc.py")

def my_func():
    x = float(input("Enter real positive number: "))
    y = int(input("Enter negative integer: "))
    a = 1
    i = -1
    while i >= y:
        x = 1 / x
        a = a * x
        x = 1 / a
        i -= 1
    return a

print(round(my_func(), 3))
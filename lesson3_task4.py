def my_func():
    x = float(input("Enter real positive number: "))
    y = int(input("Enter negative integer: "))
    z = x ** y
    return z

print(round(my_func(), 3))
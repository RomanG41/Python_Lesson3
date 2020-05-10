def fact(n):
    val = 1
    for i in range(1, n + 1):
        val *= i
        yield val


n = int(input("Укажите факториал какого числа Вы хотели бы узнать?  "))
j = 0
for el in fact(n):
    j += 1
    print(f"Факториал числа {j} равен {el}")



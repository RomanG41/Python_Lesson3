class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data_first = input("Введите делимое: ")
inp_data_second = input("Введите делитель: ")

try:
    inp_data_first = int(inp_data_first)
    inp_data_second = int(inp_data_second)
    if inp_data_second == 0:
        raise OwnError("Нельзя делить на ноль!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Частное чисел: {round(inp_data_first / inp_data_second, 2)}")
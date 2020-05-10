from random import randrange
my_list = [randrange(2, 50, 2) for i in range(20)]
print(f"Исходный список псевдослучайных чисел: {my_list}")
new_list = [i for i in my_list if my_list.count(i) == 1]
print(f"Итоговый список: {new_list}")
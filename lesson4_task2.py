my_list = [500, 355, 100, 34, 55, 67, 27, 27, 35, 78, 7, 12, 21, 3]
print(f"Исходный список: {my_list}")

new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(f"Новый список: {new_list}")




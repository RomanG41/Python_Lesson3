from sys import argv

script_name, first_param, second_param, third_param, \
fourth_param, fifth_param, sixth_param = argv

print("Имя скрипта: ", script_name)
print("Оклад работника: ", first_param, "руб.")
print("Количество календарных дней в месяце: ", second_param)
print("Количество отработанных дней в месяце: ", third_param)
print("Премия / надбавки: ", fourth_param, "руб.")
print("Процент подоходного налога: ", fifth_param)
print("Удержания: ", sixth_param, "руб.")
print("Заработная плата: ", round(int(first_param) / int(second_param) * int(third_param) + int(fourth_param)
      - (int(first_param) / int(second_param) * int(third_param) + int(fourth_param)) * int(fifth_param) / 100 - int(sixth_param), 2), "руб.")
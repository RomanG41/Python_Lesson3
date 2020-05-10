from itertools import islice, count, cycle

first_list = [i for i in islice(count(3), 10)]
print(f"Спиcок а) : {first_list}")
second_list = [i for i in islice(cycle(first_list), 25)]
print(f"Спиcок б) : {second_list}")


from random import randrange

with open("sum_num_gen.txt", "w") as fanc_gen:
    my_list = [randrange(7, 35, 3) for i in range(15)]
    sum = 0
    for i in my_list:
        sum += i
        print(i,end = ' ', file = fanc_gen)
    print(f"Сумма чисел в файле: {sum}")


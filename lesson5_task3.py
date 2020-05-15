with open('text_3.txt', 'r', encoding='utf-8') as sal_f:
    workers = {}
    all_sal = 0
    i = 0
    for line in sal_f:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(f'{key}: зарплата меньше 20000 руб.')
        i += 1
        all_sal += float(value)
    print(f"Средняя величина дохода сотрудников: {all_sal / i} руб.")










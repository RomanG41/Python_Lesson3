en_ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4.txt', 'r', encoding='utf-8') as en_fanc:
    tran_nums = []
    for line in en_fanc.readlines():
        ru_line = line.split()
        ru_line[0] = en_ru_dict[ru_line[0]]
        tran_nums.append(f'{ru_line[0]} {ru_line[1]} {ru_line[2]}\n')
    with open('tran_nums.txt', 'w', encoding='utf-8') as ru_fanc:
        ru_fanc.writelines(tran_nums)
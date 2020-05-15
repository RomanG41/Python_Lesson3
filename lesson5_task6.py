with open('text_6.txt', 'r', encoding='utf-8') as les_fanc:
    les_dict = {}
    for line in les_fanc.readlines():
        val_line = line.split()
        sub_l = [int(s) for s in val_line[1].split("(") if s.isdigit()]
        sub_l_el = sum([sum(map(int, sub_l)) for i in sub_l])
        sub_pr = [int(s) for s in val_line[2].split("(") if s.isdigit()]
        sub_pr_el = sum([sum(map(int, sub_pr)) for i in sub_pr])
        sub_lab = [int(s) for s in val_line[3].split("(") if s.isdigit()]
        sub_lab_el = sum([sum(map(int, sub_lab)) for i in sub_lab])
        les_dict[val_line[0]] = int(sub_l_el) + int(sub_pr_el) + int(sub_lab_el)
    print(les_dict)
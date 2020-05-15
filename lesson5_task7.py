import json

with open('text_7.txt', 'r', encoding='utf-8') as prof_fanc:
    prof_dict = {}
    av_dict = {}
    for line in prof_fanc.readlines():
        val_line = line.split()
        profit = int(val_line[2]) - int(val_line[3])
        prof_dict[val_line[0]] = profit
    sum1 = sum(prof_dict[item] for item in prof_dict if prof_dict[item] > 0)
    pos_count = 0
    for item in prof_dict:
        if prof_dict[item] >= 0:
            pos_count += 1
    av_prof = sum1 / pos_count
    av_dict["average_profit"] = av_prof
    prof_list = []
    prof_list.append(prof_dict)
    prof_list.append(av_dict)

with open("text_77.json", "w",  encoding='utf-8') as write_f:
    json.dump(prof_list, write_f, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
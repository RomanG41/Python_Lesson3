try:
    with open("out_file.txt", "w") as out_f:

        while True:
            content = out_f.write(input())
            out_f.write("\n")
            if not content:
                break

except IOError:
    print("Произошла ошибка ввода-вывода!")

count = open("out_file.txt", "r")
lines = [x for x in count.readlines() if x != "\n"]
count.seek(0)
words = [i for i in count.read().split()]
count.seek(0)
letters = [j for j in count.read() if j != "\n" and j != " "]
print(f"В текстовом файле {len(lines)} строк(и)")
print(f"В текстовом файле {len(words)} слов(а)")
print(f"В текстовом файле {len(letters)} букв(ы)")




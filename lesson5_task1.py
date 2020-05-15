try:
    with open("out_file.txt", "w") as out_f:

        while True:
            content = out_f.write(input())
            out_f.write("\n")
            if not content:
                break
except IOError:
    print("Произошла ошибка ввода-вывода!")


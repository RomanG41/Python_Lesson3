def total():
    total = 0
    while True:
        numbers = input('Enter list of number or Q to exit: ').split()
        for n in numbers:
            try:
                if n == 'Q':
                    print(f'Total sum is {total}. Exit')
                    return
                else:
                    total += int(n)
            except ValueError:
                print('Enter number or Q')
        print(f'Total sum is {total}')

total()
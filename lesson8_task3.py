class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def user_list():
    user_list = []
    while True:
        user_num = input('Enter a number or Q to exit: ')
        try:
            if user_num.isdigit() != True and user_num != 'Q':
                raise OwnError("Only numbers!")
            else:
                if user_num != 'Q':
                    user_list.append(user_num)
        except OwnError as err:
            print(err)
        if user_num == 'Q':
            print(f'Your list of numbers: {user_list}. Exit')
            return


user_list()

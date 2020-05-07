def data_func():
    user_data = {"name": " ", "surname": " ", "birth": " ", "city": " ", "E-mail": " ", "phone": " "}
    for i in user_data.keys():
        data_val = input(f'Enter value "{i}": ')
        user_data[i] = data_val
    return user_data

print(data_func())




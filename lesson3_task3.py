def max_func(var_1, var_2, var_3):
    """Finding the sum of two biggest.

    Params:
    var_list -- list of numbers
    numbers are entered by user

    """
    var_list = [var_1, var_2, var_3]
    var_list.remove(min(var_list))
    return sum(var_list)

print(max_func(var_1 = float(input('Enter var1: ')), var_2 = float(input('Enter var2: ')), var_3 = float(input('Enter var3: '))))
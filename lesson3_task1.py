def my_div():
    divis_val = input("Enter divisible: ")
    divid_val = input("Enter divider: ")
    try:
        divis_val = int(divis_val)
        divid_val = int(divid_val)
        pri_val = divis_val / divid_val
        return pri_val
    except ZeroDivisionError:
        return 'No / ZeroDivision!!'
    except ValueError:
        return 'Value!! Str!!'
print((my_div()))





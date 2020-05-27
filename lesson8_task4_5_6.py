class TechnicWarehouse:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'UnitPrice': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'


    def reception(self):

        try:
            unit = input(f'Enter the name ')
            unit_p = int(input(f'Enter the unitprice '))
            unit_q = int(input(f'Enter the quantity '))
            unique = {'Model of technic': unit, 'UnitPrice': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current list -\n {self.my_store}')
        except:
            return f'Data-entry error'

        print(f'For exit - Q, continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Entire warehouse -\n {self.my_store_full}')
            return f'Exit'
        else:
            return TechnicWarehouse.reception(self)


class Printer(TechnicWarehouse):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(TechnicWarehouse):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(TechnicWarehouse):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


office_equip_1 = Printer('Samsung', 4500, 7, 12)
office_equip_2 = Scanner('Epson', 2200, 3, 9)
office_equip_3 = Copier('Brother', 3100, 6, 12)
print(office_equip_1.reception())
print(office_equip_2.reception())
print(office_equip_3.reception())
print(office_equip_1.to_print())
print(office_equip_3.to_copier())
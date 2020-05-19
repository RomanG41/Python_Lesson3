class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_position(self):
        return self.position

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Ivan', 'Ivanov', 'CEO', '200000', '50000')
print(p.get_full_name(), p.get_position(), p.get_total_income())
p = Position('Petr', 'Petrov', 'DS', '150000', '30000')
print(p.get_full_name(), p.get_position(), p.get_total_income())
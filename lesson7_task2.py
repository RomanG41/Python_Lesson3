from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Всего затрачено ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Any abstract'


class Coat(Clothes):
    def consumption(self):
        return f'Чтобы пошить пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Any abstract second'


class Costume(Clothes):
    def consumption(self):
        return f'На костюм мы потратим: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(200)
costume = Costume(77)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())
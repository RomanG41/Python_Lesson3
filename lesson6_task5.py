class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")

s = Stationery("канцелярскими принадлежностями")
s.draw()

p = Pen("ручкой")
p.draw()

pn = Pencil("карандашом")
pn.draw()

h = Handle("маркером")
h.draw()
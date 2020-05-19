class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость! Ваша скорость {self.speed} км/ч'
        else:
            return f'\nВаша скорость {self.speed} км/ч, превышения нет'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость! Ваша скорость {self.speed} км/ч'
        else:
            return f'\nВаша скорость {self.speed} км/ч, превышения нет'

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass


town = TownCar('Subaru Tribeca', 'бежевый', 65, False)
print('Первый:\n' + town.go(), town.show_speed(), town.turn('направо'), town.turn('налево'), town.turn('налево'), town.stop())

police = PoliceCar('Toyota Supra', 'чёрный', 230, True)
print('Второй:\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())

sport = SportCar('Subaru Impreza WRX STI', 'синий с золотым', 250, False)
print('Третий:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('ZAZ', 'красный', 25, False)
print('Четвертый:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())


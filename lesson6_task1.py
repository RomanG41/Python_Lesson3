from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        j = 1
        while j <= 5:

            for i in range(len(TrafficLight.__color)):
                print(TrafficLight.__color[i])
                if i == 0:
                    sleep(7)
                elif i == 1:
                    sleep(2)
                elif i == 2:
                    sleep(5)

            for i in reversed(range(1, len(TrafficLight.__color) - 1)):
                print(TrafficLight.__color[i])
                if i == 1:
                    sleep(2)
                else:
                    sleep(5)
                j += 1

t = TrafficLight()
t.running()

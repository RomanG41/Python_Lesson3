class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass = 25
        self.thickness = 10

    def asphalt_coating(self):
        asphalt_coating = self._length * self._width * self.mass * self.thickness / 1000
        print(f"Для покрытия асфальтом дорожного полотна длиной {self._length} "
              f"метров,\nшириной {self._width} метров и толщиной {self.thickness} "
              f"сантиметров,\nнеобходимо {round(asphalt_coating)} тонн асфальта")

ac = Road(10000, 40)
ac.asphalt_coating()
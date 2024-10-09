from threading import Thread as Th
from time import sleep as slp

class Knight(Th):
    def __init__(self, name, power, enemies = 100, fight_days = 0):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies
        self.fight_days = fight_days

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.fight_days += 1
            self.enemies -= self.power
            print(f"{self.name}, сражается {self.fight_days} день(дня)..., осталось {self.enemies} воинов.")
            slp(1)
        print(f"{self.name} одержал победу спустя {self.fight_days} дней(дня)!")

# Алгоритм выполнения кода:

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
threads = list((first_knight, second_knight))
for t in threads:
    t.start()

for t in threads:
    t.join()

print('Все битвы закончились!')

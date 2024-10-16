from threading import Thread as Th
import queue
from time import sleep
from random import randint as rnd

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Th):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        delay = rnd(3, 11)
        sleep(delay)

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue_ = queue.Queue()

    def guest_arrival(self, *guests):
        indicator = 0
        for guest in guests:
            if indicator < len(self.tables):
                if not self.tables[indicator].guest:
                    self.tables[indicator].guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {self.tables[indicator].number}")
            else:
                self.queue_.put(guest)
                print(f"{guest.name} в очереди")
            indicator += 1

    def discuss_guests(self):
        while not self.queue_.empty():
            for table in self.tables:
                if table.guest is None:
                    table.guest = self.queue_.get()
                    table.guest.start()
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                elif not table.guest.is_alive() and table.guest:
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
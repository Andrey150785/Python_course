import threading
from random import randint
from time import sleep

lock = threading.Lock()


class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for _ in range(100):
            amount = randint(50, 501)
            self.balance += amount
            if self.balance >= 500 and lock.locked():
                lock.release()
                return None
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = randint(50, 501)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            if self.balance < amount:
                print(f'Запрос отклонён, недостаточно средств')
                lock.acquire()
                return None


# Исходный код:

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


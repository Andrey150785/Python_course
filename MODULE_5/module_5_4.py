class House():
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.name =  args[0]
        cls.houses_history.append(cls.name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor: int) ->int:
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
            return
        elif new_floor < 1:
            print('Нет лифтов в этом здании')
        for i in range(1, new_floor+1):
            print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Некорректное значение')
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Некорректное значение')
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Некорректное значение')
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Некорректное значение')
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Некорректное значение')
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Некорректное значение')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        else:
            print('Некорректное значение')
        return self
    def __radd__(self, value):
        self.__add__(value)
        return self
    def __iadd__(self, value):
        self.__add__(value)
        return self



# Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

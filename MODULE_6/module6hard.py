class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = True

    def __init__(self, color, *args):
        self.__color = self.set_color(*color)
        self.set_sides(*args)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r=-1, g=-1, b=-1):
        return all([0 <= i <= 255 for i in [r, g, b]])

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return self.__color
        else:
            return False

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count and all([i > 0 for i in sides]):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        pp = 0.5 * (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2])
        return (pp * (pp - self.get_sides()[0]) * (pp - self.get_sides()[1]) * (pp - self.get_sides()[2])) ** 0.5


class Circle(Figure):
    sides_count = 1
    def get_radius(self):
        self.__radius = self.get_sides()[0]
        print(self.__radius)
        return self.__radius / (2 * 3.14)
    def get_square(self):
        return 3.14 * self.get_radius() ** 2


class Cube(Figure):
    sides_count = 12
    def get_volume(self):
        return self.__sides[0] ** 3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = [new_sides[0] for i in range(self.sides_count)]
        else:
            pass

    def get_sides(self):
        return self.__sides


# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

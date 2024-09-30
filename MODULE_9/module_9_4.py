# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
same_letter = lambda x, y: x == y

# Test
print(list(map(same_letter, first, second)))

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything

# Test
write = get_advanced_writer('example.txt')
print(write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке']))

# Метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args):
        return choice(self.words)

# Test
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

def add_everything_up(a, b):

    try:
        result = a+b
    except TypeError as exc:
        if isinstance(a, int|float|str) and isinstance(b, int|float|str):
            result = str(a) + str(b)
            return result
        else:
            print("Неизвестный тип аргумента.Введите число или строку")
    else:
        return f'{result:.3f}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


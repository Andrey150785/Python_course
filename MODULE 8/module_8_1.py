def add_everything_up(a, b):

    try:
        result = a+b
    except TypeError as exc:
        result = str(a) + str(b)
        return result
    else:
        return f'{result:.3f}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


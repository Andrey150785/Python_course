def custom_write(file_name, strings):
    strings_positions = {} # {(<номер строки>, <байт начала строки>): строка}
    string_number = 0
    strings_position = 0
    with open(file_name, 'a', encoding='utf-8') as file:
        for string in strings:
            string_position = file.tell()
            string_number += 1
            strings_positions[(string_number, string_position)] = string
            file.write(string + '\n')

    return strings_positions

# Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


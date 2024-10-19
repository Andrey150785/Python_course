import multiprocessing
import struct
import ctypes
import multiprocessing.shared_memory

shm = multiprocessing.shared_memory.SharedMemory(create=True, size=32)
shared_data = shm.buf

# Запись строки
string_value = "Hello!"
encoded_string = string_value.encode('utf-8')  # Кодируем строку в байты
shared_data[:len(encoded_string)] = encoded_string  # Записываем байты

# Чтение строки
decoded_string = shared_data[:len(encoded_string)].tobytes().decode('utf-8')  # Читаем байты и декодируем обратно в строку
print(decoded_string)  # Hello!

string = "HelloWorld"  # длина 10 символов
size_in_bytes = len(string.encode('utf-8'))  # кодируем строку и определяем длину в байтах

import array
array_of_ints = array.array('i', [1, 2, 3, 4])  # массив из 4 целых чисел (4 байта на каждый)
size_in_bytes1 = len(array_of_ints) * 4

# Создаем массив из целых чисел
arr = array.array('i', [5, 6, 7, 8])
print(arr)  # array('i', [1, 2, 3, 4])

# Преобразуем массив в байты
arr_bytes = arr.tobytes()
print(arr_bytes)  # b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00'
# Чтение массива из байтов
new_arr = array.array('i')  # создаем пустой массив того же типа
new_arr.frombytes(arr_bytes)  # загружаем байты в массив
print(new_arr)  # array('i', [1, 2, 3, 4])

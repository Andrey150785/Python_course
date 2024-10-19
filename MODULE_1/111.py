import multiprocessing.shared_memory
import struct

def crypto_utils(block):
    # Пример: функция шифрования возвращает строку и число с плавающей точкой
    unique_string = "ABCDEFGH"  # фиксированная 8-символьная строка (замените на реальную логику)
    quality_metric = 99.99  # фиксированное значение для качества шифрования
    return unique_string, quality_metric

shm = multiprocessing.shared_memory.SharedMemory(create=True, size=32)
shared_data = shm.buf

string_, float_= crypto_utils("block1")
print(string_, float_)

# exit()

# задаем большое значение
shared_data[:len(string_)] = string_.encode('utf-8')
read_data = shared_data[:len(string_)].tobytes().decode()
print(read_data)
# int_value = struct.unpack('i', shared_data[0:4])[0]
# print(int_value)

# изменяем значение
shared_data[len(string_):] = struct.pack('d', float_)
# float_value = struct.unpack('f', shared_data[0:4])[0]
# print(float_value)
exit()
# -99988
# 123999
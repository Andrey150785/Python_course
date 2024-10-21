import multiprocessing
import struct
import ctypes
from multiprocessing import Process, shared_memory

class Encrypter(Process):
    def __init__(self, shm: shared_memory, target, args):
        super().__init__()
        self.target = target
        self.args = args
        # Создаем разделяемую память для строки (8 символов = 16 байт)
        # и числа с плавающей запятой (8 байт)
        self.buffer = shm.buf


    def run(self):
        string_value, float_value = self.target(*self.args)
        encoded_string = string_value.encode('utf-8')
        string_len = len(encoded_string) # кодируем строку
        self.buffer[:string_len] = encoded_string
        self.buffer[string_len:string_len+8] = struct.pack('d', float_value)
        result1 = self.buffer[:string_len].tobytes().decode('utf-8')
        result2 = struct.unpack('d', self.buffer[string_len:string_len+8])[0]
        print(result1, result2)# используем struct для записи float

    # def get_result(self):
    #     # Извлекаем строку (16 байт) и число с плавающей точкой (8 байт)
    #     string_value = buffer[:16].tobytes().decode('utf-16')  # извлекаем строку
    #     float_value = struct.unpack('d', self.buffer[16:24])[0]  # извлекаем float
    #     return string_value, float_value

def crypto_utils(block):
    # Пример: функция шифрования возвращает строку и число с плавающей точкой
    unique_string = "ABCDEFGH"  # фиксированная 8-символьная строка (замените на реальную логику)
    quality_metric = 99.99  # фиксированное значение для качества шифрования
    return unique_string, quality_metric

def main():
    shm = multiprocessing.shared_memory.SharedMemory(create=True, size=24)
    text_blocks = ["block1", "block2", "block3"]  # пример данных для шифрования
    results = {}

    # Создаем процессы для шифрования
    # processes = [Encrypter(target=crypto_utils, args=(block,), shm=shm) for block in text_blocks]
    proc = Encrypter(target=crypto_utils, args=(text_blocks[0],), shm=shm)
    proc.start()

    # Запускаем процессы
    # for process in processes:
    #     process.start()
    #
    # # Ожидаем завершения процессов
    # for process in processes:
    #     process.join()

    # Извлекаем результаты из разделяемой памяти
    # for process in processes:
        # result = process.get_result()  # кортеж (строка, число с плавающей точкой)
        # results[result] = process.args[0]

    print(results)

if __name__ == "__main__":
    main()

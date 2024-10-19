import multiprocessing
import struct
import ctypes
import multiprocessing.shared_memory

class Encrypter(multiprocessing.Process):
    def __init__(self, target, args=()):
        super().__init__()
        self.target = target
        self.args = args
        # Создаем разделяемую память для строки (8 символов = 16 байт) и числа с плавающей запятой (8 байт)
        self.shm = multiprocessing.shared_memory.SharedMemory(create=True, size=24)
        self.result_buf = self.shm.buf

    def run(self):
        res = self.target(*self.args)  # результат в виде кортежа (строка, число с плавающей точкой)
        string_value, float_value = res

        # Записываем строку (16 байт, т.к. каждый символ занимает 2 байта в UTF-16)
        encoded_string = string_value.encode('utf-16')  # кодируем строку
        self.result_buf[:16] = encoded_string[:16]  # заполняем первые 16 байт

        # Записываем число с плавающей точкой (8 байт)
        self.result_buf[16:24] = struct.pack('d', float_value)  # используем struct для записи float

    def get_result(self):
        # Извлекаем строку (16 байт) и число с плавающей точкой (8 байт)
        string_value = self.result_buf[:16].tobytes().decode('utf-16')  # извлекаем строку
        float_value = struct.unpack('d', self.result_buf[16:24])[0]  # извлекаем float
        return string_value, float_value

def crypto_utils(block):
    # Пример: функция шифрования возвращает строку и число с плавающей точкой
    unique_string = "ABCDEFGH"  # фиксированная 8-символьная строка (замените на реальную логику)
    quality_metric = 99.99  # фиксированное значение для качества шифрования
    return unique_string, quality_metric

def main():
    text_blocks = ["block1", "block2", "block3"]  # пример данных для шифрования
    results = {}

    # Создаем процессы для шифрования
    processes = [Encrypter(target=crypto_utils, args=(block,)) for block in text_blocks]

    # Запускаем процессы
    for process in processes:
        process.start()

    # Ожидаем завершения процессов
    for process in processes:
        process.join()

    # Извлекаем результаты из разделяемой памяти
    for process in processes:
        result = process.get_result()  # кортеж (строка, число с плавающей точкой)
        results[result] = process.args[0]

    print(results)

if __name__ == "__main__":
    main()

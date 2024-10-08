import time
from datetime import datetime
import threading

def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        counter = 0
        for i in range(word_count):
            counter += 1
            file.write(f"Какое-то слово № {counter}" + '\n')
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")
        return

# Проверка работы кода и измерение времени выполнения программы с использованием 1 главного потока
start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
print(f'Работа потоков {datetime.now() - start} # Может быть другое время')


# Проверка работы кода и измерение времени выполнения программы с использованием 4 потоков
start = datetime.now()
th1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
th2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
th3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
th4 = threading.Thread(target=write_words, args=(100, "example8.txt"))
th1.start()
th2.start()
th3.start()
th4.start()
th1.join()
th2.join()
th3.join()
th4.join()
print(f'Работа потоков {datetime.now() - start} # Может быть другое время')
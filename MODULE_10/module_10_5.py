import datetime
import multiprocessing

# with open('file 1.txt', 'r', encoding='utf-8') as file:
#     print(file.read())
#     exit()

list_of_numbers = [f'file {i}.txt' for i in range(1, 5)]
proc_count = multiprocessing.cpu_count()
print('Повторение строки')


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        file_data = file.readline()
        while file_data:
            file_data = file.readline()
            # if file line:  # Если строка пустая, прекращаем чтение
            #     break
            all_data.append(file_data.strip())
    return all_data


start = datetime.datetime.now()
for file in list_of_numbers:
    read_info(file)

end = datetime.datetime.now() - start
print(end) # 0:00:09.469433


# Проверка работы кода и измерение времени выполнения программы с использованием multyprocessing
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool( processes = 4) as pool:
        results = pool.map(read_info, list_of_numbers)
    end = datetime.datetime.now() - start
    print(end)  # 0:00:11.240079

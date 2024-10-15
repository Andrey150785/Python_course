import datetime
import multiprocessing

list_of_numbers = [f'file {i}.txt' for i in range(1, 5)]
proc_count = multiprocessing.cpu_count()

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        file_data = file.readlines()
        for line in file_data:
            if not line:  # Если строка пустая, прекращаем чтение
                break
            all_data.append(line.strip())
    return all_data


start = datetime.datetime.now()
for file in list_of_numbers:
    read_info(file)

end = datetime.datetime.now() - start
print(end) # 0:00:09.469433


# Проверка работы кода и измерение времени выполнения программы с использованием multyprocessing
start = datetime.datetime.now()
if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        results = pool.map(read_info, list_of_numbers)
end = datetime.datetime.now() - start
print(end)  # 0:00:11.240079

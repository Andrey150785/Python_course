import datetime
import multiprocessing

list_of_numbers = [fr'.\Files\file {i}.txt' for i in range(1, 5)]
proc_count = multiprocessing.cpu_count()
print(f'Количество процессоров: {proc_count}')


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        file_data = file.readlines()
        for line in file_data:
            all_data.append(line.strip())
    return all_data


# start = datetime.datetime.now()
# for file in list_of_numbers:
#     read_info(file)
#
# end = datetime.datetime.now() - start
# print(end) # 9.743046600007801 / 0:00:09.469433


# Проверка работы кода и измерение времени выполнения программы с использованием multyprocessing
start = datetime.datetime.now()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=proc_count) as pool:
        pool.map(read_info, list_of_numbers)
    end = datetime.datetime.now() - start
    print(end)  # 0.000000000000000000e+00 / 0:00:00.000000

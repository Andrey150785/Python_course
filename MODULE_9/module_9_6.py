
def all_variants(text):
    for i in range(1, len(text)+1):
        start_ind = 0
        end_ind = start_ind + i
        while end_ind <= len(text):
            res = text[start_ind:end_ind]
            yield res
            start_ind += 1
            end_ind += 1
        else:
            continue
 
#Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
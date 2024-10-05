def apply_all_func(int_list: list|tuple, *functions):
    result = dict()
    for func in functions:
        result[func.__name__] = func(int_list)
    return result

res = apply_all_func([1, 2, 3, 4, 5], min, max, len, sorted, sum)
print(res)
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


print(object)
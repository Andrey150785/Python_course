def is_prime(func):
    def wrapper(*args, **kwargs):
        cifr = 'Простое'
        res = func(*args, **kwargs)
        for i in range(2, res):
            if res % i == 0:
                cifr = 'Составное'
                break
            else:
                continue
        print(cifr)
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

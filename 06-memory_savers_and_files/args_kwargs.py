def my_function(*param_1):
    print(type(param_1))
    return param_1


print(my_function('string', 'string2'))

def numbers_sum(*var):
    suma = 0
    print(var)
    for item in var:
        suma += item
    return suma


print(numbers_sum(1, 2, 3, 4, 6))


def diff_vars(*params):
    diff = 0
    for item in params:
        diff -= params
    return diff


def catalog(**kwargs):
    print(type(kwargs))
    return kwargs.keys()


catalog()
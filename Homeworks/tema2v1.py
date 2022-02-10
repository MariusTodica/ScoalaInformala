def your_function(*args):
    suma = 0
    for i in args:
        if type(i) == int:
            suma = suma + i
    print(f"Prima suma: {suma}")

def your_function1(*args, param_a):
    suma = 0
    for i in args:
        try:
            suma = suma + int(i)
        except ValueError:
            pass
        except TypeError:
            pass
    print(f"A doua suma: {suma}")

your_function(1, 5, -3, 'abc', [12, 56, 'cad'])
your_function1(2, 4,'abc', param_a = 2)
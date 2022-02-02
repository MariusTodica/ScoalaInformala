#Functii:
# print("Afisam mesaj")
# format()
# a = input("X")
#
# def functiea_mea():
#     pass

def suma(a: int, b: int = 1, c: int=0) -> (int, int):
    """

    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of params, dif of params
    """
    return a + b + c, a - b - c

var_1 = 1
var_2 = 2
sum, dif = suma(a = var_1, b = var_2, c = 0)
print(sum, dif)
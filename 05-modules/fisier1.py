# import primul_modul
# import math
# from math import "sumeeeeee"
# from primul_modul import my_sum as suma (as suma uneori)
# from primul_modul import my_sum
# if __name__ == '__main__':
#     print(my_sum(4, 5))
    # print(primul_modul.my_sum(1, 4))

my_var = input("Numar intreg: ")
my_int = None
try:
    my_int = int(my_var)
except Exception as e:
    my_int = 'test'
    print("Exceptie generica", e)
else:
    print("Daca nu apare exceptie", my_int)
finally:
    print("Afiseaza in orice caz")
print(my_int)

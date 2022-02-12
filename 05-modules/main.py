# print() # str
# input() # str
# "".format() # str

# def functie2():
#     my_function()
#
#
# def my_function():
#     # function body
#     # return None
#     pass
#
# print(functie2())



# def message():
#     print("Enter a value")
#
# message()

# def my_function(a: str, b: str , c: str) -> str:
#     return a, b, c


# print(my_function(a = '1', c = '2', b = '3'))
# print(my_function(1', '3', '2'))
# print(my_function('1', c='2', b='3'))
# print(my_function('3', a='1', c='2')) # asa nu
# print(my_function('1', '3', c='2'))


# def my_function():
#     pass
#
# a = my_function()
# print(a)
# b = None
# print(type(b))

# def my_function(n):
#     if n % 2 == 0:
#         return True
#
# # print(my_function(3))
# nr = input("Introdu nr: ")
# if my_function(int(nr)) is True:
#     print("Nr este divizibil")
# elif my_function(int(nr)) is False:
#     print("Nr nu este divizibil")


# def my_function():
#     return f"Cunosti aceasta variabila: {var}"
#
# var = 1
# print(my_function())
# print(var)

# lista = [1, 2, 3 , [4, 5, [6, 7]]]
#
# print(lista[3][2][0])

# try:
#     # bloc de expresii
# except:
#     # daca apare o exceptie si vrem sa afisam ceva

try:
    valoare = int(input("Prima cifra din CNP: "))
    impartire = 1/valoare
except ValueError:
    print("Ai introdus litera")
except ZeroDivisionError:
    print("Eroare la impartire")
except Exception as e:
    print("Exceptie la impartire", e)
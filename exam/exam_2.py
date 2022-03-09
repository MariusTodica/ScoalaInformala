lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
while lista:
    j = 0
    for i in lista:
        if j % 2 == 0:
            lista.remove(i)
        j += 1
    print(f"Lista: {lista}")
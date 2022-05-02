def adunare(n):
    return n + n


lista_numere_1 = [1, 2, 3, 4, 5]
lista_numere_2 = [5, 6, 7, 8, 9, 10]
rezultat = map(adunare, lista_numere_1)
print(list(rezultat))

rezultat_2 = map(lambda n: n + n, lista_numere_1)
print(list(rezultat_2))

rezultat_3 = map(lambda n, m: n + m, lista_numere_1, lista_numere_2)
print(list(rezultat_3))


def adunare(lista_numere_1, lista_numere_2):
    suma = 0
    lista_adunare = []
    for i, v in enumerate(lista_numere_1):
        for j, w in enumerate(lista_numere_2):
            if i == j:
                # suma = lista_numere_1[i] + lista_numere_2[j]
                suma = v + w
                lista_adunare.append(suma)
    return lista_adunare


def adunare_2(lista_numere_1, lista_numere_2):
    suma = 0
    lista_adunare = []
    for i in range(0, min(len(lista_numere_1), len(lista_numere_2))):
        lista_adunare.append(lista_numere_1(i) + lista_numere_2(i))
    return lista_adunare

print(adunare(lista_numere_1, lista_numere_2))
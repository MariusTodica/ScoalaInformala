# Reguli
# Daca primul caracter si ultimul se repetau in cuvant, caracterul trebuia afisat
# Restul caracterelor erau ascunse
# 7 sanse de a ghici cuvantul (dupa 7 murim)
# word = o _ o _ _ _ o _ e e
word = 'onomatopee'
# litera_cuvant = input("Alege o litera")
# print(litera_cuvant)
lista_cuvant = []
for iterator in word:
    lista_cuvant.append('_')
    print(iterator, word[0], word[-1])
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1] = iterator
print(' '.join(lista_cuvant))
numar_incercari = 1
lista_litere_incercate = set()
while numar_incercari <= 7:
    litera = input("Alege o litera: ").lower()
    if litera.lower() in word.lower():
        for index, valoare in enumerate(word):
            if valoare.lower() == litera.lower():
                lista_cuvant[index] = litera
    else:
        print('Litera nu exista, deja ai 'f'incercat urmatoarele litere {",".join(lista_litere_incercate)}')
        print(f"Mai ai {7 - numar_incercari} incercari")
        if litera.lower() not in lista_litere_incercate:
            numar_incercari += 1
        lista_litere_incercate.add(litera)
    if 8 - int(numar_incercari) == 0:
        print(f"Ai pierdut! Cuvantul era {word}")
    elif ''.join(lista_cuvant) == word:
        print("Ai castigat!")
    else:
        print(' '.join(lista_cuvant))

# k
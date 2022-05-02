lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numere_pare(number):
    if number % 2 == 0:
        return True
    return False


iterator_numere_pare = filter(numere_pare, lista_numere)
print(iterator_numere_pare)

litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def filter_vocale(letter):
    vocale = ['a', 'e', 'i']
    return True if letter in vocale else False

filtrare_vocale = filter(filter_vocale, litere)
print(list(filtrare_vocale))
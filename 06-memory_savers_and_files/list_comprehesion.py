lista = [item for item in 'Ana are mere']
print(lista)


list_produse = ['ciocolata', 'suc', 'mere', 'apa']

new_list = [x if x != 'suc' else 'apa minerala' for x in list_produse]
print(new_list)
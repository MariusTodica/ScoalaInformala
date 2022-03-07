# cream fisierele
# cream sa bage de la tastatura: task, data, nume, categorie(sa exista o singura data categoria)
# sa afisam categoriile disponibile


import csv
# import pandas as pd
global all_categories, all_items


def add_category():
    category_list = []
    global all_categories
    active = input("Doresti sa adaugi categorii?[y/n]: ")
    active.lower()
    while active == 'y':
        category = input("Introdu o categorie: ")
        if category not in category_list:
            category_list.append(category)
        else:
            print("Categoria exista! Incearca din nou.")
        active = input('Vrei sa mai adaugi? [y/n]: ')
    print("\nLista de categorii s-a format!")
    all_categories = []
    all_categories = category_list
    with open("lista.csv", "w") as file:
        for item in category_list:
            file.write(item)
    print(f'\n {category_list}')


def add_list():
    active = True
    global all_items
    all_items = []
    items = []
    while active:
        task = input("Introdu un task: ")
        limita = input("Introdu o data limita (ex: 02.10.2020 21:30): ")
        responsabil = input("Introdu un responsabil (ex: ex: Ion Vasile): ")
        category = input("Introdu o categorie: ")

        with open("lista.csv", "r") as file:
            for line in list(file):
                if category in line:
                    continue
                else:
                    category = input(f"Categoria nu exista!\n Categoriile disponibile - {all_categories} -\n "
                                     "Introdu o categorie: ")
                if not line:
                    break

        item = [task, limita, responsabil, category]
        items.append(item)

        all_items = items
        print(all_items)

        with open('out.csv', 'w') as file_out:
            csv_writer = csv.writer(file_out, delimiter=',')

            for item in items:
                csv_writer.writerow(item)

        again = input('Mai adaugi un task? [y/n]: ')
        again.lower()
        if again == 'n':
            active = False
        else:
            continue


def listare_date():
    print(all_items)


def options():
    # print(f"Meniu:\n1. Listare date\n"
    #                 "2. Sortare\n"
    #                 "3. Filtrare date\n"
    #                 "4. Adaugare task nou\n"
    #                 "5. Editare task\n"
    #                 "6. Stergere task\n")
    print("Meniu: ")
    option = {
        1: 'Listare date\n',
        2: 'Sortare\n',
        3: 'Filtrare date\n',
        4: 'Adaugare task nou\n',
        5: 'Editare\n',
        6: 'Stergere\n'
    }

    option = []
    option = int(input("Introduceti ce optiune doriti: "))
    if option in range(7):
        return True
    else:
        return options()


def list_date():
    print("Ati ales optiune 1")
    category_sort = []
    for item in all_items:
        aux = item[3]
        category_sort.append(aux)
    category_sort.sort()
    print(category_sort)


def sortare_date():
    # options = {1: "sortare ascendentă task",
    #            2: "sortare descendentă task",
    #            3: "sortare ascendentă data",
    #            4: "sortare descendentă data",
    #            5: "sortare ascendentă persoana responsabilă",
    #            6: "sortare descendentă persoană responsabilă",
    #            7: "sortare ascendentă categorie",
    #            8: "sortare descendentă categorie"}

    print(f"Meniu:\n1. Sortare ascendentă task\n"
                   "2. Sortare descendentă task\n"
                   "3. Sortare ascendentă data\n"
                   "4. Sortare descendentă data\n"
                   "5. Sortare ascendentă persoana responsabilă\n"
                   "6. Sortare descendentă persoană responsabilă\n"
                   "7. Sortare ascendentă categorie\n"
                   "8. Sortare descendentă categorie\n")

    option = int(input("Introduceti ce optiune doriti: "))
    print(f"Ati ales optiunea: {option}")
    if option == 1:
        task_sort = []
        for item in all_items:
            aux = item[0]
            task_sort.append(aux)
        task_sort.sort()
        print(task_sort)

    elif option == 2:
        task_sort = []
        for item in all_items:
            aux = item[0]
            task_sort.append(aux)
        task_sort.sort()
        print(task_sort[::-1])

    elif option == 3:
        limita_sort = []
        for item in all_items:
            aux = item[1]
            limita_sort.append(aux)
        limita_sort.sort()
        print(limita_sort)

    elif option == 4:
        limita_sort = []
        for item in all_items:
            aux = item[1]
            limita_sort.append(aux)
        limita_sort.sort()
        print(limita_sort[::-1])

    elif option == 5:
        responsabil_sort = []
        for item in all_items:
            aux = item[2]
            responsabil_sort.append(aux)
        responsabil_sort.sort()
        print(responsabil_sort)

    elif option == 6:
        responsabil_sort = []
        for item in all_items:
            aux = item[2]
            responsabil_sort.append(aux)
        responsabil_sort.sort()
        print(responsabil_sort[::-1])

    elif option == 7:
        categorie_sort = []
        for item in all_items:
            aux = item[1]
            categorie_sort.append(aux)
        categorie_sort.sort()
        print(categorie_sort)

    elif option == 8:
        categorie_sort = []
        for item in all_items:
            aux = item[1]
            categorie_sort.append(aux)
        categorie_sort.sort()
        print(categorie_sort[::-1])


def delete_task():
    alegere = str(input("Ce task doriti sa stergeti?"))
    print(f"Lista: {all_items}")
    for item in all_items:
        if alegere in item[0]:
            if item[0] == alegere:
                all_items.pop(item)

    return all_items


def choice(choicex):
    if choicex == 1:
        return list_date()
    elif choicex == 2:
        return sortare_date()
    elif choicex == 3:
        return
    elif choicex == 4:
        return
    elif choicex == 5:
        return
    elif choicex == 6:
        return delete_task()
    return False




# def options():
#     # print("1. Listare date")    -   listare_date()
#     # print("2. Sortare")         -   sortare_date()
#     # print("3. Filtrare date")
#     # print("4. Adaugare task nou")
#     # print("5. Editare")
#     # print("6. Sterge un task")
#
#     print("Meniu: ")
#     list_options = [
#         '1. Listare date\n',
#         '2. Sortare\n',
#         '3. Filtrare date\n',
#         '4. Adaugare task nou\n',
#         '5. Editare\n',
#         '6. Stergere'
#     ]
#
#     option1 = print(list_options)
#     option = input("Introdu o optiune: ")
#     # while option != 0:
#     if option in range(1, 7):
#         return True
#     else:
#         option = int(input("Introdu o optiune valida: "))
#
#     item = [task, limita, responsabil, category]
#     # tabel_list = pd.DataFrame(item)
#
#     if list_options == '1':
#         # tabel_list.sort_values(item)
#         print(tabel_list)


# def meniu():
#     global list_options
#     if list_options == 1:

# add_category()
# add_list()
# options()

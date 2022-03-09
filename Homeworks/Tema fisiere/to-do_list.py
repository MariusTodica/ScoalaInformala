import csv
import datetime
global all_items, all_categories, option, options


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


def add_tasks():
    active = True
    global all_items
    all_items = []
    items = []
    while active:
        task = input("Introdu un task: ")
        limita = input("Introdu o data limita (ex: 02.10.2020): ")
        datetime.datetime.strptime(limita, "%d.%m.%Y")
        responsabil = input("Introdu un responsabil (ex: Ion Vasile): ")
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


def meniu():
    print("""Meniu: 
        1. Listare date
        2. Sortare
        3. Filtrare date
        4. Adaugare task nou
        5. Editare
        6. Stergere""")


def choice(meniu):
    choices = {
        1: 'Listare date',
        2: 'Sortare',
        3: 'Filtrare date',
        4: 'Adaugare task nou',
        5: 'Editare',
        6: 'Stergere'
    }

    if option in range(7):
        print(f"Optiunea aleasa: {choices[option]}")
        return True
    else:
        return meniu()


def list_date():
    global all_items
    print("Ati ales optiunea 1")
    categorie_sort = []
    for item in all_items:
        aux = item[3]
        categorie_sort.append(aux)
    categorie_sort.sort()
    print(categorie_sort)


def sortare_date():
    print(f"""Meniu: 1. Sortare ascendentă task
       2. Sortare descendentă task
       3. Sortare ascendentă data
       4. Sortare descendentă data
       5. Sortare ascendentă persoana responsabilă
       6. Sortare descendentă persoană responsabilă
       7. Sortare ascendentă categorie
       8. Sortare descendentă categorie""")

    opt = int(input("Introduceti ce optiune doriti: "))
    print(f"Ati ales optiunea: {opt}")
    if opt == 1:
        task_sort = []
        for item in all_items:
            aux = item[0]
            task_sort.append(aux)
        task_sort.sort()
        print(task_sort)

    elif opt == 2:
        task_sort = []
        for item in all_items:
            aux = item[0]
            task_sort.append(aux)
        task_sort.sort()
        print(task_sort[::-1])

    elif opt == 3:
        limita_sort = []
        for item in all_items:
            aux = item[1]
            limita_sort.append(aux)
        limita_sort.sort()
        print(limita_sort)

    elif opt == 4:
        limita_sort = []
        for item in all_items:
            aux = item[1]
            limita_sort.append(aux)
        limita_sort.sort()
        print(limita_sort[::-1])

    elif opt == 5:
        responsabil_sort = []
        for item in all_items:
            aux = item[2]
            responsabil_sort.append(aux)
        responsabil_sort.sort()
        print(responsabil_sort)

    elif opt == 6:
        responsabil_sort = []
        for item in all_items:
            aux = item[2]
            responsabil_sort.append(aux)
        responsabil_sort.sort()
        print(responsabil_sort[::-1])

    elif opt == 7:
        categorie_sort = []
        for item in all_items:
            aux = item[1]
            categorie_sort.append(aux)
        categorie_sort.sort()
        print(categorie_sort)

    elif opt == 8:
        categorie_sort = []
        for item in all_items:
            aux = item[1]
            categorie_sort.append(aux)
        categorie_sort.sort()
        print(categorie_sort[::-1])


def filtrare_date():
    return


def edit_task():
    print(all_items)
    alegere = int(input("Ce task doriti sa editati? "))
    var = list(all_items[alegere])
    print(f"Taskul pe care l-ati ales este: {var}")
    print("""Ce doriti sa schimbati?
    1. Nume task
    2. Limita
    3. Nume responsabil
    4. Categoria""")
    x = int(input("Alegere: "))  # 2 - limita
    if x == 1:
        y = input("Introduceti un nume de task nou: ")
        var.insert(x, y)
    if x == 2:
        y = input("Introduceti o limita noua: ")
        var.insert(x, y)
    if x == 3:
        y = input("Introduceti un responsabil nou: ")
        var.insert(x, y)
    if x == 4:
        print(f"Categorii existente: {all_categories}")
        y = input("Introduceti o categorie: ")
        var.insert(x, y)
        while y not in all_categories:
            y = input("Introduceti o categorie: ")


def delete_task():
    print(all_items)
    alegere = int(input("Ce task doriti sa stergeti? "))
    all_items.pop(alegere)
    print(f"Lista task-uri actualizata: {all_items}")


# def choice():
#     # add_category()
#     # add_tasks()
#     meniu()
#     if option == 1:
#         return list_date()
#     elif option == 2:
#         return sortare_date()
#     elif option == 3:
#         return filtrare_date()
#     elif option == 4:
#         return add_tasks()
#     elif option == 5:
#         return edit_task()
#     elif option == 6:
#         return delete_task()


if __name__ == '__main__':
    add_category()
    add_tasks()
    meniu()
    option = int(input("Alegere: "))
    choice(option)
    if option == 1:
        list_date()
    elif option == 2:
        sortare_date()
    elif option == 3:
        filtrare_date()
    elif option == 4:
        add_tasks()
    elif option == 5:
        edit_task()
    elif option == 6:
        delete_task()

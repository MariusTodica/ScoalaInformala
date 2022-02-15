my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

asc = my_list.copy()
asc.sort()
print(f"Ascendent: {asc}, \nDescendent: {asc[::-1]}")

my_list.sort()
my_sliced_list1 = my_list[1::2]
my_sliced_list2 = my_list[::2]
print(f"Numere pare: {my_sliced_list1}, \nNumere impare: {my_sliced_list2}")

multiplu = my_list[2::3]
print(f"Multipli nr 3: {multiplu}")













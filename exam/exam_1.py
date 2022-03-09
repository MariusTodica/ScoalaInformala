x = int(input("Introduceti primul nr: "))
y = int(input("Introduceti al 2-lea nr: "))
z = int(input("Introduceti al 3-lea nr: "))

suma = x + y + z

if x == y == z:
    print(f"{suma}\n"*3)
else:
    print(f"{suma}")

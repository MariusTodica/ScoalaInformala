def my_function():
    n = input("Introduceti un numar: ")
    try:
        n = int(n)
        return f"Numarul introdus este: {n}"
    except ValueError:
        return 0

print(my_function())

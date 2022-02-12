# 2 variabile
# 1 operator
# 1 rezultat

def suma(a: int, b: int) -> str:
    return f"{a} + {b} = {a + b}"


def diferenta(a, b) -> str:
    return f"{a} - {b} = {a - b}"


def inmultire(a: int, b: int) -> str:
    return f"{a} * {b} = {a * b}"


def impartire(a: int, b: int) -> str:
    if b == 0:
        while b == 0:
            b = int(input("Aloca o noua valoare: "))
    if a % b == 0:
        return f"{a} / {b} = {a / b}"


def operator() -> str:
    op = input("Alege operatorul: ")
    if op not in ['*', '/', '+', '-']:
        return op
        while op not in ['*', '/', '+', '-']:
            op = input("Alege operatorul: ")
    return op


def calculator():
    nr1 = int(input("Primul nr: "))
    nr2 = int(input("Al doilea nr: "))
    op = operator()
    if op == '+':
        rezultat = sum(nr1, nr2)
    elif op == '-':
        rezultat = diferenta(nr1, nr2)
    elif op == '*':
        rezultat = inmultire(nr1, nr2)
    else:
        rezultat = impartire(nr1, nr2)
    return rezultat

print(calculator())
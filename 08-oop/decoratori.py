# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
#
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"
#
#
# print(functie_simpla())
# "".join()

# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def ambalaj_intern(*args):
#             # print(f"Ambalam produse din {functia_noastra.__name__} cu {material}")
#             return f'Ambalam produse din {functia_noastra.__name__} cu {material}: {", ".join(x for x in functia_noastra(*args))}'
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit("hartie")
# def impachetare_carti(*args):
#     return args
#
#
# @decorator_depozit("folie_alimentara")
# def impachetare_fructe(*args):
#     return args
#
#
# print(impachetare_carti("Amintiri din copilarie", "Baltagul"))
# print(impachetare_fructe("mere", "pere"))


def decorator(functie):
    def decoreaza(var):
        return functie(var)
    return decoreaza

def p(functie):
    def decoreaza(var):
        return f"<p>{functie(var)}</p>"
    return decoreaza

@p
def text(sir):
    return sir.upper()


# text_p = decorator(text)
print(text("Salut"))

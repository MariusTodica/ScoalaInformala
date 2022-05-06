from operator import itemgetter


class CatalogPrajituri:

    lista_prajituri = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        prajituri = [self.nume, self.pret, self.gramaj]
        self.lista_prajituri.append(prajituri)

    @staticmethod
    def sortare_gramaj():
        prajituri_gramaj = sorted(CatalogPrajituri.lista_prajituri, key=itemgetter(2))
        return f"Prajiturile in functie de pret sunt {prajituri_gramaj}"

    @staticmethod
    def sortare_pret():
        prajituri_pret = sorted(CatalogPrajituri.lista_prajituri, key=itemgetter(1))
        return f"Prajiturile in functie de pret sunt {prajituri_pret}"

    def __str__(self):
        return f"Prajitura {self.nume} avand pretul {self.pret} lei, cu un gramaj de {self.gramaj} grame."


class Tort(CatalogPrajituri):

    def __init__(self, nume, pret, gramaj, etajat = False, glazura = "ciocolata"):
        super().__init__(nume, pret, gramaj)
        self.etajat = etajat
        self.glazura = glazura

    def __str__(self):
        return f"Tortul {self.nume} are o glazura de {self.glazura} fiind etajat {self.etajat}, avand un pret de {self.pret} lei si un gramaj de {self.gramaj} grame."


class Fursec(CatalogPrajituri):

    def __init__(self, nume, pret, gramaj):
        super().__init__(nume, pret, gramaj)

    def __str__(self):
        return f"Fursecul {self.nume}, avand un pret de {self.pret} lei si un gramaj de {self.gramaj} grame."


prajitura1 = CatalogPrajituri("Eclere", 10, 300)
prajitura2 = CatalogPrajituri("Lava Cake", 21, 150)
prajitura3 = CatalogPrajituri("Tiramisu", 35, 750)

tort1 = Tort("Black Forest", 82, 1150, etajat=True, glazura="cacao")
tort2 = Tort("Oreo", 91, 950, etajat=False, glazura="Nutella")
tort3 = Tort("Apple Caramel", 67, 1250, etajat=False, glazura="Caramel")

fursec1 = Fursec("Vanilla Cookie", 12, 100)
fursec2 = Fursec("Oat Cookie", 31, 450)
fursec3 = Fursec("Chocolate Cookie", 25, 350)

print(prajitura1)
print(prajitura2)
print(prajitura3)
print(tort1)
print(tort2)
print(tort3)
print(fursec1)
print(fursec2)
print(fursec3)
print("\n")
print(CatalogPrajituri.sortare_pret())
print("\n")
print(CatalogPrajituri.sortare_gramaj())


from operator import itemgetter

class Catalog_Prajituri:
    lista_prajituri = []
    def __init__(self, nume = "Chec", pret = 100, gramaj = 400):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        caracteristici_obiect = [self.nume, self.pret, self.gramaj]
        self.lista_prajituri.append(caracteristici_obiect)

    @staticmethod
    def sortare_pret():
        sortata_pret = sorted(Catalog_Prajituri.lista_prajituri, key=itemgetter(1))
        return f"Prajiturile sortate dupa pret sunt {sortata_pret}"

    @staticmethod
    def sortare_gramaj():
        sortata_gramaj = sorted(Catalog_Prajituri.lista_prajituri, key=itemgetter(2))
        return f"Prajiturile sortate dupa gramaj sunt {sortata_gramaj}"

class Tort(Catalog_Prajituri):
    def __init__(self, nume, gramaj, pret, etajat = False, glazura = "ciocolata"):
        super().__init__(nume, gramaj, pret)
        self.etajat = etajat
        self.glazura = glazura

    def __str__(self):
        return f"Etajarea este {self.etajat} iar glazura este {self.glazura}"

class Fursec(Catalog_Prajituri):
    pass
    # def __init__(self):
    #     super().__init__()

prj1=Catalog_Prajituri("Eclere", 10, 300)
prj2=Catalog_Prajituri("Ecler mic", 7, 115)
prj3=Catalog_Prajituri("Lava", 15, 275)

tort1 = Tort(nume = "A", gramaj = 112, pret = 150, etajat = True, glazura = "cacao")
tort2 = Tort(nume = "D", gramaj = 55, pret = 45, etajat = True, glazura = "cacao")
tort3 = Tort(nume = "B", gramaj = 1150, pret = 350, etajat = True, glazura = "cacao")

fursec1 = Fursec()
# print(fursec1.nume)

print(Catalog_Prajituri.lista_prajituri)

print(Catalog_Prajituri.sortare_gramaj())

# print(Catalog_Prajituri.sortare_pret())


# print(tort1.glazura)
# print(tort1.gramaj)
# print(tort1.nume)
#
# print(tort1)
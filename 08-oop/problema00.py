class Calcul:
    def __init__(self, a=1, b=2, c=3, d=4 ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def verificare(self):
        self.e = f"Informatiile introduse nu sunt cifre"
        if str(self.a).isnumeric() and str(self.b).isnumeric()and str(self.c).isnumeric() and str(self.d).isnumeric():
            self.e = (self.a * (self.b + 3) / self.c) * self.d
        return self.e

    def __str__(self):
        return f"Rezultatul este: {self.verificare()}"

obiect = Calcul()
print(obiect)
obiect2=Calcul(5,6,7,8)
print(obiect2)
obiect3 = Calcul("x","y","z",2)
print(obiect3)
obiect4 = Calcul(9,2)
print(obiect4)
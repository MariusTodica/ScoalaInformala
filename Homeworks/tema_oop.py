class Util:
    y = []

    def __init__(self, obiect):
        self.obiect = obiect
        y.append(obiect)

    def __str__(self):
        return f'Obiectul: {self.y}'

    # @staticmethod
    # def __vars__(self, x):
    #     y.append(self.x)
    #     return y

# x = Util('a')
# y = Util('b')
# z = Util('c')
# a = Util('h')
# print(a)


class Izatori:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw

    def __str__(self):
        return f"Userul este: {self.user},\nParola este: {self.passw}"


# print(Izatori('alune', 'marar'))

class Utilizatori(Util, Izatori):
    global useri, parole

    def __init__(self, obiect, user, passw):
        super().__init__(user, passw, obiect)
        # super().__init__(obiect)

    @staticmethod
    def __useri__(user):
        useri.add(user)
        return useri

    @staticmethod
    def __parole__(passw):
        parole.add(passw)
        return parole


creion = Util("crein")
sdas = Izatori("Ion", "pasr")
crein = Utilizatori('Asss', 'Saaaa', 'ddd')
print(crein)

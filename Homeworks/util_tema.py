# class Util:
#
#     __util_list = []
#
#     def __init__(self, obiect):
#         self.obiect = obiect
#
#
# class Izatori:
#
#     def __init__(self, user, passw):
#         self.user = user
#         self.passw = passw

class Util:

    __util_list = []

    def __init__(self, obiect='Creion'):
        self.obiect = obiect

    def __str__(self):
        mesaj = f'Obiectul cautat este {self.obiect}'
        return mesaj

print(f'{__util_list}')
#
# class Izatori(Util):
#
#
#     def __init__(self, obiect, user, passw):
#         super().__init__.(obiect)
#         self.user = user
#         self.passw = passw
#
#     def __str__(self):
#         mesaj1 = f''
#
#
# class Utilizatori(Util, Izatori):
#
#     def __init__(self, ):

# class TelefonFix(Telefon):
#
#     last_sn = 0
#
#     def __init__(self, numar):
#         super().__init__(numar)
#         TelefonFix.last_sn += 1
#         self.SN = f"Telefon fix - {TelefonFix.last_sn}"
#
#
# class TelefonMobil(Telefon):
#
#     last_sn = 0
#
#     def __init__(self, numar):
#         super().__init__(numar)
#         TelefonMobil.last_sn += 1
#         self.SN = f"Telefon mobil - {TelefonMobil.last_sn}"
#
#
# print(f"Numarul total de dispozitive este {Telefon.counter}")
# fix_1 = TelefonFix('021 77 66 55')
# fix_2 = TelefonFix('031 66 33 88')
# mobil = TelefonMobil('0741 45 67 89')
# print(f"Numarul total de dispozitive fixe este {TelefonFix.last_sn}")
# print(f"Numarul total de dispozitive mobile este {TelefonMobil.last_sn}")
# print(f"Numarul total de dispozitive este {Telefon.counter}")class Telefon:
from datetime import datetime


class CNP:

    def __init__(self, cnp):
        self.cnp = cnp

    def lungime(self):
        return len(self.cnp) != 13 or not self.cnp.isdigit()

    def sex(self):
        return int(self.cnp[0]) in range(1, 10)

    def data_nașterii(self):
        try:
            datetime.strptime(self.cnp[1:7], "%y%m%d")
            return True
        except ValueError:
            return False

    def judet(self):
        return self.cnp[7:9] in ["%02d" % i for i in range(1, 47)] or int(self.cnp[7:9]) in [51, 52]

    def nnn(self):
        return self.cnp[9:12] in ["%03d" % i for i in range(1, 1000)]

    def cifra_de_control(self):
        n = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
        suma = 0
        for i, j in zip(self.cnp[:12], n):
            suma += int(i) * j
        a = suma % 11
        c = a
        if a == 10:
            c = 1
        return int(self.cnp[12]) == c

    def validare(self):
        if not self.cnp.isdigit():
            return "\nAti introdus un CNP invalid."
        elif self.sex() and self.data_nașterii() and self.judet() and self.nnn() and self.cifra_de_control():
            return "\nAti introdus un CNP valid."
        return "\nAti introdus un CNP invalid."


cnp_1 = CNP("")
print(cnp_1.validare())
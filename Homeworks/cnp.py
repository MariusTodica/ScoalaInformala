# S AA LL ZZ JJ NNN C

import random

def cnp():
    global s, aa, ll, zz, reg, nnn, c, z
    gen = input("Introdu genul(B/F): ")
    an = int(input("Introdu anul nasterii: "))
    luna = input("Introdu luna nasterii: ")
    ziua = input("Introdu ziua nasterii: ")
    judet = input("Introdu judetul: ")

    s = 0

    regiuni = {1: "alba",
             2: "arad",
             3: "arges",
             4: "bacau",
             5: "bihor",
             6: "bistrita-nasaud",
             7: "botosani",
             8: "brasov",
             9: "braila",
             10: "buzau",
             11: "caras-severin",
             12: "cluj",
             13: "constanta",
             14: "covasna",
             15: "dambovita",
             16: "dolj",
             17: "galati",
             18: "gorj",
             19: "harghita",
             20: "hunedoara",
             21: "ialomita",
             22: "iasi",
             23: "ilfov",
             24: "maramures",
             25: "mehedinti",
             26: "mures",
             27: "neamt",
             28: "olt",
             29: "prahova",
             30: "satu mare",
             31: "salaj",
             32: "sibiu",
             33: "suceava",
             34: "teleorman",
             35: "timis",
             36: "tulcea",
             37: "vaslui",
             38: "valcea",
             39: "vrancea",
             40: "bucuresti",
             41: "bucuresti s.1",
             42: "bucuresti s.2",
             43: "bucuresti s.3",
             44: "bucuresti s.4",
             45: "bucuresti s.5",
             46: "bucuresti s.6",
             51: "calarasi",
             52: "giurgiu"
             }

    luni = {1: "ianuarie", 2: "februarie", 3: "martie", 4: "aprilie", 5: "mai", 6: "iunie",
            7: "iulie", 8: "august", 9: "septembrie", 10: "octombrie", 11: "noiembrie", 12: "decembrie"
            }
    luni_zi = {"ianuarie": 31, "februarie": 28, "martie": 31, "aprilie": 30, "mai": 31, "iunie": 30, "iulie": 31, "august": 31,
            "septembrie": 30, "octombrie": 31, "noiembrie": 30, "decembrie": 31}

    gen.lower()
    judet.lower()
    luna.lower()

    if 1900 < int(an) < 1999:
        if gen == "b":
            s = 1
        else:
            s = 2
    if 2000 < int(an) < 2099:
        if gen == "b":
            s = 5
        else:
            s = 6

    aa = an % 100

    if 0 < aa < 10:
        k = str(aa)
        aa = k.zfill(2)

    luni_keys = luni.keys()
    luni_list = list(luni_keys)
    luni_values = luni.values()
    luni_listval = list(luni_values)

    ll = luna

    if luna in luni_listval:
        index = luni_listval.index(luna)
        ll = luni_list[index]
        if 0 < int(ll) < 10:
            k = str(ll)
            ll = k.zfill(2)

    zz = ziua

    if 0 < int(zz) < 10:
        k = str(zz)
        zz = k.zfill(2)


    regiuni_keys = regiuni.keys()
    regiuni_list = list(regiuni_keys)
    regiuni_values = regiuni.values()
    regiuni_listval = list(regiuni_values)

    if judet in regiuni_listval:
        index = regiuni_listval.index(judet)
        reg = regiuni_list[index]
        if 0 < reg < 10:
            k = str(reg)
            reg = k.zfill(2)

    nnn = str(random.randint(0o01, 1000))
    nnn.zfill(4)

    luni_zi_keys = luni_zi.keys()
    luni_zi_list = list(luni_zi_keys)
    luni_zi_values = luni_zi.values()
    luni_zi_listval = list(luni_zi_values)

    if luna in luni_zi_list:
        index = luni_zi_list.index(luna)
        k = luni_zi_listval[index]
        if 0 < int(zz) < k:
            z = 0
        else:
            z = 1
            
    validare = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma = 0
    t = f"{s}{aa}{ll}{zz}{reg}{nnn}"
    y = list(t)
    for i in y:
        for j in validare:
            if i == j:
                suma += int(y[i]) * validare[j]
    rest = suma % 11
    if rest == 10:
        c = 1
    else:
        c = rest
    cnp = f"{s}{aa}{ll}{zz}{reg}{nnn}{c}"
    print(f"CNP-ul rezultat este: {cnp}")

    if len(cnp) == 13 and 1900 < an < 2099 and z == 0:
        print("CNP valid!")
    else:
        print("CNP invalid!")

cnp()

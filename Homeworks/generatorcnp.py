def cnp():
    global zz_max
    cnp_input = input("Introduceti cnp-ul: ")
    gen = cnp_input[0]
    aa = cnp_input[1:3]
    ll = cnp_input[3:5]
    zz = int(cnp_input[5:7])
    jj = cnp_input[7:9]
    nnn = cnp_input[9:11]
    c = cnp_input[12]
    corect = bool

    gen_list = ['1', '2', '5', '6']

    judet = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
             '11', '12', '13', '14', '15', '16', ' 17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
             '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
             '41', '42', '43', '44', '45', '46', '51', '52']

    luni = {
        '01': 31,
        '02': 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    luni_keys = luni.keys()
    luni_list = list(luni_keys)
    luni_values = luni.values()
    luni_listval = list(luni_values)

    if 0 < int(aa) < 100:
        if ll in luni_list:
            index = luni_list.index(ll)
            zz_max = luni_listval[index]
            if 0 < zz < zz_max:
                if gen in gen_list:
                    corect = True
                else:
                    corect = False
                    print(f"Sex incorect!")
            else:
                corect = False
                print(f"Zi incorecta!")
        else:
            corect = False
            print(f"Luna incorecta!")
    else:
        corect = False
        print(f"An incorect!")
    if jj in judet:
        corect = True
    else:
        corect = False
        print("Judet incorect!")

    if 0 < int(nnn) < 1000:
        corect = True
    else:
        corect = False
        print("Numar secvential incorect!")

    validare = ['2', '7', '9', '1', '4', '6', '3', '5', '8', '2', '7', '9']
    val_c = cnp_input[0:12]
    len_validare = len(validare)
    len_val_c = len(val_c)
    suma = 0
    for i in range(len_validare):
        for j in range(len_val_c):
            if i == j:
                suma = suma + int(validare[i]) * int(val_c[j])
    rest = suma % 11
    if rest == 10:
        cc = 1
    else:
        cc = rest
    if 0 < int(c) < 10 and int(c) == cc:
        corect = True
    else:
        corect = False
        print("Cifra de control incorecta!")

    print(f"Status cnp: {corect}")

cnp()
dictionar = {"1": "abc", "2": "s","3": "o","4": "n","5": "lm","6": "jk","7": "gi","8": "def","9": "abc"}

x = dictionar.values()
list_1 = []
list_2 = []
list_3 = []
list_final = []

for i in x:
    if len(i) == 2:
        list_2.append(i)
    if len(i) == 1:
        list_1.append(i)

for i in x:
    if len(i) == 1:
        a = i
        for j in x:
            if len(j) == 1 and a != j:
                p = str(a+j)
                list_3.append(p)

list_final = list_2 + list_3
print(f"Lista cu 2 cifre: {list_final}")

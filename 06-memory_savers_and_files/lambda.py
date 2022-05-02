my_lambda = lambda x, y: x + y
# denumire functie = lambda param1, param2: corp functie


def my_lambda(x, y):
    return x + y

my_sum = my_lambda(2, 4)
print(my_sum)


players = [{
    'first_name': 'Ion',
    'last_name': 'Gheorghe',
    'varsta': 12
}, {
    'first_name': 'Andreea',
    'last_name': 'Popa',
    'varsta': 35
    }, {
    'first_name': 'Isabela',
    'last_name': 'Enache',
    'varsta': 25
    }
]

jucatori_sortati = sorted(players, key=lambda player: player['varsta'])

print(jucatori_sortati)
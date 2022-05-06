import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np


dataset = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84', ': ']),
    ('AT', ['75', '79', '81', '81', '82', '85', '89', '89', '90']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69', '72']),
    ('BE', ['77', '78', '80', '83', '82', '85', '86', '87', '90']),
    ('BG', ['45', '51', '54', '57', '59', '64', '67', '72', '75']),
    ('CH', [': ', ': ', ': ', '91', ': ', ': ', '93', ': ', '96']),
    ('CY', ['57', '62', '65', '69', '71', '74', '79', '86', '90']),
    ('CZ', ['67', '73', '73', '78', '79', '82', '83', '86', '87']),
    ('DE', ['83', '85', '88', '89', '90', '92', '93', '94', '95']),
    ('DK', ['90', '92', '93', '93', '92', '94', '97', '93', '95']),
    ('EA', ['74', '76', '79', '81', '83', '85', '87', '89', '90']),
    ('EE', ['69', '74', '79', '83', '88', '86', '88', '90', '90']),
    ('EL', ['50', '54', '56', '66', '68', '69', '71', '76', '79']),
    ('ES', ['63', '67', '70', '74', '79', '82', '83', '86', '91']),
    ('FI', ['84', '87', '89', '90', '90', '92', '94', '94', '94']),
    ('FR', ['76', '80', '82', '83', '83', '86', '86', '89', '90']),
    ('HR', ['61', '66', '65', '68', '77', '77', '76', '82', '81']),
    ('HU', ['63', '67', '70', '73', '76', '79', '82', '83', '86']),
    ('IE', ['78', '81', '82', '82', '85', '87', '88', '89', '91']),
    ('IS', ['93', '95', '96', '96', ': ', ': ', '98', '99', '98']),
    ('IT', ['62', '63', '69', '73', '75', '79', '81', '84', '85']),
    ('LT', ['60', '60', '65', '66', '68', '72', '75', '78', '82']),
    ('LU', ['91', '93', '94', '96', '97', '97', '97', '93', '95']),
    ('LV', ['64', '69', '72', '73', '76', '77', '79', '82', '85']),
    ('ME', [': ', '55', ': ', ': ', ': ', ': ', '71', '72', '74']),
    ('MK', [': ', '58', '65', '68', '69', '75', '74', '79', '82']),
    ('MT', ['75', '77', '78', '80', '81', '81', '85', '84', '86']),
    ('NL', ['94', '94', '95', '96', '96', '97', '98', '98', '98']),
    ('NO', ['92', '93', '94', '93', '97', '97', '97', '96', '98']),
    ('PL', ['67', '70', '72', '75', '76', '80', '82', '84', '87']),
    ('PT', ['58', '61', '62', '65', '70', '74', '77', '79', '81']),
    ('RO', ['47', '54', '58', '61', '68', '72', '76', '81', '84']),
    ('RS', [': ', ': ', ': ', ': ', '64', ': ', '68', '73', '80']),
    ('SE', ['91', '92', '93', '90', '91', '94', '95', '93', '96']),
    ('SI', ['73', '74', '76', '77', '78', '78', '82', '87', '89']),
    ('SK', ['71', '75', '78', '78', '79', '81', '81', '81', '82']),
    ('TR', [': ', '47', '49', '60', '70', '76', '81', '84', '88']),
    ('UK', ['83', '87', '88', '90', '91', '93', '94', '95', '96']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89', '93', '93']),
    ]

years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']


def get_year_data(set_data, year):
    values = []
    for data in set_data:
        country = data[0]
        info = data[1]
        y = years.index(year)
        value = info[y]
        output = (country, value)
        values.append(output)
    x = {year: values}
    return x


# print(get_year_data(dataset, '2019'))


def get_country_data(set_data, country):
    values = []
    for data in set_data:
        if data[0] == country:
            values = list(zip(years, data[1]))
    output = {country: values}
    return output


# print(get_country_data(dataset, 'RO'))


def perform_average(country_data):
    summ = 0
    cont = 0
    for data in dataset:
        if data[0] == country_data:
            for i in data[1]:
                def int_check(h):
                    try:
                        h = int(h)
                    except ValueError:
                        h = 0
                    finally:
                        return h
                i = int_check(i)
                cont += 1
                summ += i
    med = summ / cont
    result = ("{:.2f}".format(med))
    return result


# print(perform_average('RO'))


def struct_date(dates):

    all_data, countries, dict_country, output, all_values = [], [], {}, {}, {}
    for d in dates:
        countries.append(d[0])
    for data in dates:
        values = []
        w = 0
        country = data[0]
        for i in data[1]:
            def int_check(h):
                try:
                    h = int(h)
                except ValueError:
                    h = 0
                finally:
                    return h

            dict_country = {'year': years[w],
                            'coverage': int_check(i)}
            values.append(dict_country)
            w += 1

        data_set = {country: values}
        all_data.append(data_set)

    # for x in all_data:
        # print(x)

    with open('out.csv', 'w', newline='') as csvfile:
        fieldnames = ('Country', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', 'Average')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in all_data:
            coverr = []
            country = list(x.keys())[0]
            listt = x.values()
            for n in listt:
                for a in n:
                    g = a.get('coverage')
                    f = g
                    coverr.append(f)

            med = perform_average(country)
            x['average'] = med

            writer.writerow({'Country': country, '2011': coverr[0], '2012': coverr[1],
                             '2013': coverr[2], '2014': coverr[3], '2015': coverr[4],
                             '2016': coverr[5], '2017': coverr[6], '2018': coverr[7],
                             '2019': coverr[8], 'Average': med})
        csvfile.close()

    x = pd.DataFrame(dataset)
    # print(x.describe())


first = dataset[0][0]
second = dataset[1][0]
x = [first, second]

# y = [perform_average(first), perform_average(second)]
# plt.scatter(x, y, c='blue')
# plt.show()


ro_values = []

for i in dataset:
    if i[0] == 'RO':
        for j in i[1]:
            def int_check(h):
                try:
                    h = int(h)
                except ValueError:
                    h = 0
                finally:
                    return h
            ro_values.append(int_check(j))
# print(ro_values)

# p = np.array(ro_values, dtype=object)
# p = ([1, 2, 3, 4, 5, 6])
#
# ro_values, bins, patches = plt.hist(x=years, y=p, bins=9, color='#0504aa', alpha=1, rwidth=0.5)
# plt.grid(axis='both', alpha=1)
# plt.xlabel('Ani')
# plt.ylabel('Valori')
# plt.title('Romania')
# valori = ro_values.all()
# plt.ylim(ymax=np.ceil(valori) if type(valori) == int else valori)

plt.hist(years, (0, 10), ec="red")

plt.xlabel("Ani")
plt.ylabel("Valori")
plt.title("Romania")
plt.show()

struct_date(dataset)
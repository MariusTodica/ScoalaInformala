# import os
import csv
import json


# for file_name in [file for file in os.listdir('output_data') if os.path.isfile('output_data')]:
#     os.remove('output_data')

cars = []
brands_list = []

with open('input.csv', 'r+') as file_in:
    csv_reader = csv.reader(file_in)
    for car in [[csv_reader.line_num, row[0], row[1], int(row[2]), int(row[3])] for row in csv_reader]:
        cars.append({key: value for(key, value) in zip(['id', 'brand', 'model', 'hp', 'price'], car)})
        brands_list.append(cars[-1].get('brand'))


sorted_cars = {
    'slow_cars':        filter(lambda car: car['hp'] < 120, cars),
    'fast_cars':        filter(lambda car: 120 <= car['hp'] < 180, cars),
    'sport_cars':       filter(lambda car: car['hp'] >= 180 , cars),
    'cheap_cars':       filter(lambda car: car['price'] < 1000, cars),
    'medium_cars':      filter(lambda car: 1000 <= car['price'] < 5000, cars),
    'expensive_cars':   filter(lambda car: car['price'] >= 5000, cars)
}

for brand in brands_list:
    sorted_cars[brand] = list(filter(lambda car: car['brand'] == brand, cars))

for sorted_car in sorted_cars:
    with open(f'output_data/{sorted_car}.json', 'w') as json_file:
        json.dump(list(sorted_cars[sorted_car]), json_file)

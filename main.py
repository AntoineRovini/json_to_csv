import csv
import json


def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)

        data_list = [row for row in csv_data]
    with open(json_file, 'w') as file:
        json.dump(data_list, file, indent=4)


csv_to_json('C:\\Users\\antoi\\Documents\\code\\eNOVA\\flight_track\\al_test_format.json', 'output.json')

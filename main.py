import csv
import json

with open('file') as file:
    data = json.load(file)

response_data = data['response']

parameters = []
for response_item in response_data:
    parameters.append(list(response_item.values()))

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(parameters)

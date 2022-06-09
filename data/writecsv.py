import csv
import os

inputs = []
path = os.path.join('.', 'source.csv')
with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        inputs.append(row[1]+' @ '+row[2])
targets = []
path = os.path.join('.', 'target.csv')
with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        targets.append(row[1])
path = os.path.join('.', 'text.csv')
with open(path, 'w') as csvfile:
    fieldnames = ['inputs', 'target']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(inputs)):
        writer.writerow({"inputs": inputs[i], 'target': targets[i]})

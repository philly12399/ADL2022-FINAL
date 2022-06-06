import csv
with open('source.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)

with open('target.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)
import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)

    for row in reader:
        print(row)
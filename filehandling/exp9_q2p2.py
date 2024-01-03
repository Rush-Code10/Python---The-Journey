import csv
count = 0
with open('e-card-transacts.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)
        count = count + 1
print(count)
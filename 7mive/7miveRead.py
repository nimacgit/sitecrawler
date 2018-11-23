import csv
with open('7mivePrice.csv', newline='', encoding="utf-16") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for a in row:
            print(a)
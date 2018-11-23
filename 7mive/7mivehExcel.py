import csv

import xlsxwriter

workbook = xlsxwriter.Workbook('7mive.xlsx')
worksheet = workbook.add_worksheet("new sheet")


name = []
price = []
date = []
moredis = []
weight = []
with open('7mivePrice.csv', newline='', encoding="utf-16") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if(len(row) > 0):
            name += [int(row[0])]
            price += [row[1]]
            date += [row[2]]
            try:
                moredis += [row[3]]
            except:
                moredis += [""]
            try:
                weight += [row[4]]
            except:
                weight += [""]



for n, p in enumerate(zip(name, price, date, moredis, weight)):
        worksheet.write(n, 0, p[0])
        worksheet.write(n, 1, p[1])
        worksheet.write(n, 2, p[2])
        worksheet.write(n, 3, p[3])
        worksheet.write(n, 4, p[4])
workbook.close()





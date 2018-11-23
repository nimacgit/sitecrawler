import requests, requests.utils, pickle
from bs4 import BeautifulSoup as bs
import csv
import datetime

now = datetime.datetime.now()
file_object = open('nimac.pkl', 'rb')
cookies = requests.utils.cookiejar_from_dict(pickle.load(file_object))
request = requests.session()

url = 'https://7mive.com/shop'
resp = request.get(url, cookies=cookies, verify=False)

def numberFix(num):
    s = ""
    for ch in num:
        if(ch != ','):
            s += ch
    return int(s)


soup = bs(resp.text, 'html.parser')
name = soup.find_all(itemprop='name')
name = [x.get_text() for x in name]
price = soup.find_all(itemprop='price')
price = [numberFix(x.get_text()) for x in price]
now = str(now.year) + " " + str(now.month) + " " + str(now.day)
moredis = soup.findAll("p", {"class": "prd-desc more"})
moredis = [x.get_text() for x in moredis]
weight = soup.findAll("span", {"class": "unit"})
weight = [x.get_text() for x in weight]


with open('7mivePrice.csv', 'a', encoding="utf-16") as csvfile:
    excel = csv.writer(csvfile)
    print("test" + str(name[0]) + " " + str(price[0]))
    for a, b, c, d in zip(price, name, moredis, weight):
        excel.writerow([str(a), str(b), now, str(c), str(d)])
         #excel.writerow([str(a).encode(sys.stdout.encoding, errors='replace')] + [str(b).encode(sys.stdout.encoding, errors='replace')])

#
# workbook = xlsxwriter.Workbook('7mive.xlsx')
# worksheet = workbook.add_worksheet("new sheet")
#
# for n, p in enumerate(zip(name, price)):
#         worksheet.write(n, 0, p[0])
#         worksheet.write(n, 1, p[1])
# workbook.close()

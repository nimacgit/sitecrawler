import json
import time
from pprint import pprint

import xlsxwriter
from pandas import DataFrame

import xlwt
from bs4 import BeautifulSoup as bs
import selenium
import scrapy
import requests, requests.utils, pickle

workbook = xlsxwriter.Workbook('gradeGM2.xlsx')
worksheet = workbook.add_worksheet("new sheet")

request = requests.session()
url = 'http://calculus.math.sharif.ir/gm2_2018/Grades.php'
urlRes = 'http://calculus.math.sharif.ir/gm2_2018/Results.php?course=calc2'


def getGrade(url, cookie, id):
    data = {'ID': str(id)}
    gradeResp = request.post(url, cookies=cookie, data=data)
    soup = bs(gradeResp.text, 'html.parser')
    if (len(soup.find_all(id='M1Q1')) >= 5):
        return [(soup.find_all(id='M1Q1')[0]).get_text(), (soup.find_all(id='M1Q1')[1]).get_text(),
                (soup.find_all(id='M1Q1')[2]).get_text(), (soup.find_all(id='M1Q1')[3]).get_text(),
                (soup.find_all(id='M1Q1')[4]).get_text()]
    else:
        return [-1, -1, -1, -1, -1]


resp = request.post(url)
siteCookie = resp.cookies
id = 93100000
pos = 0
prog = 1
for i in range(10000):
    if(i >= prog):
        print(prog/10000)
        prog += 500

    try:
        l = getGrade(urlRes, siteCookie, id)
        if l[0] != -1:
            worksheet.write(pos, 0, id)
            worksheet.write(pos, 1, l[4])
            pos += 1
    except:
        pass
    # time.sleep(0.005)
    id += 1

workbook.close()

# sheet1.write(0, 0, 1)
# sheet1.write(0, 0, 2)
# sheet1.write(0, 0, "hi")
#
# book.save("trial.xls")

#
# #file_object.write((str(resp.text)))
#
# pickle.dump(requests.utils.dict_from_cookiejar(resp.cookies), file_object)
#
#
# url = 'https://7mive.com/shop'
# resp = request.post(url, cookies=resp.cookies, verify=False)
# print(resp.text)
#
# pickle.dump(requests.utils.dict_from_cookiejar(resp.cookies), file_object)
#
#
#
# # with open('somefile') as f:
# #     cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
# #     session = requests.session(cookies=cookies)
#
#
#
#
#
#
#
#
# #url = 'http://dining.sharif.ir/admin/site/logout'
# #resp = requests.post(url)
# #print(resp.text)
#
#
#
#
#
#
#
#
# # url = 'http://dining.sharif.ir/admin/food/food-reserve/reserve'
# # resp = request.post(url, cookies=resp.cookies)
#
# #print(resp.text)
#
# #url = 'http://dining.sharif.ir/admin/food/food-reserve/do-reserve-from-diet?user_id=16338'
# #url = 'http://dining.sharif.ir/admin/food/food-reserve/cancel-reserve?user_id=16338"'
# #data = {'id': '11255',
# #'place_id': '19'}
# #resp = request.post(url, data= data, cookies=resp.cookies)
#
#
# # id,url,url2,url3,place_id,food_place_id,self_id,user_id){
# # requests.Request.json()
# #
# # do_reserve_from_diet("11255",
# #                      "/admin/food/food-reserve/do-reserve-from-diet?user_id=16338",
# #                      "/admin/food/food-reserve/load-reserved-table",
# #                      "/admin/food/food-reserve/load-reserve-table",
# #                      "19", "0", "19", "16338");
#
#
# # url = 'http://dining.sharif.ir/admin/food/food-place/load-places'
# # resp = request.post(url, cookies=resp.cookies)
# #print(resp.text)
#
#
# #print(resp.text)

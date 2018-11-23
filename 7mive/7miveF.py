from selenium import webdriver
import scrapy
import requests, requests.utils, pickle
from bs4 import BeautifulSoup as bs

mobile = "09359500980"
data = {'mobile': mobile}

file_object = open("nimac.pkl", 'ab')

request = requests.session()
url = 'https://api.7mive.com/public/api/register'
resp = request.post(url, data=data, verify=False)
print(resp.text)

sms_code = input("write sms")
data = {'sms_code': sms_code, 'mobile': mobile, 'remember': 'checked'}
url = 'https://api.7mive.com/public/api/login'
resp = request.post(url, data=data, cookies=resp.cookies, verify=False)
print(resp.text)
# file_object.write((str(resp.text)))
# pickle.dump(requests.utils.dict_from_cookiejar(resp.cookies), file_object)

url = 'https://7mive.com/shop'
resp = request.get(url, cookies=resp.cookies, verify=False)

pickle.dump(requests.utils.dict_from_cookiejar(resp.cookies), file_object)

soup = bs(resp.text, 'html.parser')
name = soup.find_all(itemprop='name')
name = [x.get_text() for x in name]
price = soup.find_all(itemprop='price')
price = [x.get_text() for x in price]
for a,b in zip(name, price):
    print(str(a) + " " + str(b))



















# with open('somefile') as f:
#     cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
#     session = requests.session(cookies=cookies)


#url = 'http://dining.sharif.ir/admin/site/logout'
#resp = requests.post(url)
#print(resp.text)


# url = 'http://dining.sharif.ir/admin/food/food-reserve/reserve'
# resp = request.post(url, cookies=resp.cookies)

#print(resp.text)

#url = 'http://dining.sharif.ir/admin/food/food-reserve/do-reserve-from-diet?user_id=16338'
#url = 'http://dining.sharif.ir/admin/food/food-reserve/cancel-reserve?user_id=16338"'
#data = {'id': '11255',
#'place_id': '19'}
#resp = request.post(url, data= data, cookies=resp.cookies)


# id,url,url2,url3,place_id,food_place_id,self_id,user_id){
# requests.Request.json()
#
# do_reserve_from_diet("11255",
#                      "/admin/food/food-reserve/do-reserve-from-diet?user_id=16338",
#                      "/admin/food/food-reserve/load-reserved-table",
#                      "/admin/food/food-reserve/load-reserve-table",
#                      "19", "0", "19", "16338");


# url = 'http://dining.sharif.ir/admin/food/food-place/load-places'
# resp = request.post(url, cookies=resp.cookies)
#print(resp.text)


#print(resp.text)
import requests
import selenium
import scrapy

data = {'_csrf': 'R1B1SENEdkwjPiVwLXQ7Dy5lHDs1dwU.KwYEIAY2BRYfYDQddD4pIw==',
           'LoginForm[username]': '96100114',
        'LoginForm[password]': '0022225404'}

request = requests.session()
url = 'http://dining.sharif.ir/login'
resp = request.post(url, data=data)
#print(resp.text)




#url = 'http://dining.sharif.ir/admin/site/logout'
#resp = requests.post(url)
#print(resp.text)








url = 'http://dining.sharif.ir/admin/food/food-reserve/reserve'
resp = request.post(url, cookies=resp.cookies)

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

url = 'http://dining.sharif.ir/admin/food/food-place/load-places'
resp = request.post(url, cookies=resp.cookies)
print(resp.text)


#print(resp.text)
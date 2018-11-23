from selenium import webdriver
import requests
import pickle
from bs4 import BeautifulSoup as bs

username = "96100114"
password = "0022225404"

data = {"changeMenu: OnlineRegistration*RegistrationGuide",
        "isShowMenu:",
        "commandMessage:",
        "defaultCss: "}


driver = webdriver.Chrome()
driver.get("https://edu.sharif.edu")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
print(driver.get_cookies())

from http.cookies import SimpleCookie

rawdata = 'Cookie: _ga=GA1.2.969355752.1534482039;' \
          ' JSESSIONID=nM0Rmitqyzs4sWMMdOBXB5BDbq09pS3ilLqwUJOV1bCZv_BxQgHS!484861232'
cookie = SimpleCookie()
cookie.load(rawdata)
#driver.add_cookie(cookie_dict=cookie)

while(True):
    a = input()
    print(driver.get_cookies())

'''
command: add
lessonID: 
groupID: 
unit:


:authority: edu.sharif.edu
:method: POST
:path: /action.do?command=add
'''

'''
command: changeGroup
lessonID: 300003
groupID: 19

ttps://edu.sharif.edu/action.do?command=changeGroup&lessonID=300003&groupID=19
'''


# request = requests.session()
# url = 'https://edu.sharif.edu/action.do'
# resp = request.post(url, data=data, verify=False, cookies=cookies)
# #print(resp.text)



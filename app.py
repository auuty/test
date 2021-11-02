import requests
from bs4 import BeautifulSoup





# __RequestVerificationToken
# Tgv9reV0ddHP3RAffrHPNZgl2f6shNNLV2x9d4BboZ91O4adpAMZDuR28dwcZ-hLI5zzqGg-gTh3gaYv8ac8IwvhyXs1

urlLogin = "https://www.theanimenetwork.com/Account/Login"
urlMyAccount = "https://www.theanimenetwork.com/My/Account"
header_ = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "th,en;q=0.9",}

# proxie = {"http":"http://14.207.120.158:8080",
#           "https":"http://14.207.120.158:8080",
#           "ftp":"http://14.207.120.158:8080"}

sess = requests.session()
resp = sess.get(urlLogin, headers=header_)
print(resp.status_code)
soup = BeautifulSoup(resp.content, "Lxml")
RequestVerificationToken = soup("input")[0]["value"]
print(RequestVerificationToken)

data = {"_RequestVerificationToken" : RequestVerificationToken,
        "Username": "thanakonxx",
        "Password": "1999xnxx"}
respLogin = sess.post(urlLogin, headers=header_, data=data)
print(respLogin.status_code)

respMyAccount = sess.get(urlMyAccount, headsers=header_)
print(respMyAccount.text)
























        

















import requests as r
import random
import sys
import time as t

token = input('token: ')

headers = {
    'Authorization': token,
    'Content-type': 'application/json'
    }

json = {}

while True:
    res = r.put('https://discord.com/api/v8/users/@me/relationships/781022407745994752', headers=headers, json=json)
    if res.status_code == 403:
        print('account is already unverified - ' + str(res.status_code))
        t.sleep(3)
        sys.exit('finished')
    elif res.status_code != 403:
        print('sent')
    res = r.delete('https://discord.com/api/v8/users/@me/relationships/781022407745994752', headers=headers)
    if res.status_code != 403:
        print('deleted')
    elif res.status_code == 403:
        print('account has been unverified - ' + str(res.status_code))
    print(str(res.status_code))
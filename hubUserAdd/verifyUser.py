import requests as req
import json
from random import randint

username = input('Username>> ')
userPassword = input('Password>> ')

domain = input('Https domain name>> ')
apiKey = input('APIKEY>> ')



login = req.post(f'https://{domain}/attask/api/v10.0/login?username={username}&password={userPassword}')

fields = 'ID,emailAddr'

userIDs = []

initGet = req.get(f"https://{domain}/attask/api/v10.0/user/search?entryDate=$$TODAY&$$LIMIT=2000&fields={fields}&apiKey={apiKey}")
jsonResponse = initGet.json()



data = jsonResponse




for item in data['data']:
    userIDs.append(item['emailAddr'])






if len(userIDs) != 0:
    for index, item in enumerate(userIDs):
        verify = req.post(f"https://{domain}/resetPassword?username={item}&oldpassword=Password1&newpassword=Password1&temporary=true")
        if index % 50 == 0:
            print(f"{index} out of {len(userIDs)} verified\n\n")
    print(f'Success! {len(userIDs)} Users password is Password1')
else:
    print('No users detected to have been entered in $$TODAY')

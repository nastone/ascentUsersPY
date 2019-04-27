import requests as req
import json
from envVariables import domain, apiKey, fields
from random import randint

apiKey2 = '5q739uqd2y1t6bvfcwmdlo61jl96xemo'

userIDs = []

initGet = req.get(f"{domain}attask/api/v10.0/user/search?entryDate=$$TODAY-3d&$$LIMIT=2000&fields={fields}&companyID=4f70af2b000072ad140ec40ea11ea20b&apiKey={apiKey}")
jsonResponse = initGet.json()



data = jsonResponse


for item in data['data']:
    userIDs.append(item['emailAddr'])




if len(userIDs) != 0:
    for index, item in enumerate(userIDs):
        verify = req.post(f"{domain}resetPassword?username={item}&oldpassword=Password1&newpassword=Password1&temporary=true")
        jsonTest = verify.json()
        if index % 50 == 0:
            print(f"{index} out of {len(userIDs)} verified\n\n")
            print(jsonTest)
print(f'Success! Users password is Password1')

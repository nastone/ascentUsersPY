import json
import requests as req

domain = 'https://rileyrohloff.my.workfront.com/attask/api'
apiKey = '5q739uqd2y1t6bvfcwmdlo61jl96xemo'
fields = 'ID,emailAddr'

IDs = []


initGet = req.get(f"{domain}/v10.0/user/search?entryDate=$$TODAY&apiKey={apiKey}&fields={fields}&$$LIMIT=2000")
response = initGet.json()

data = response
userData = data['data']

for item in userData:
    IDs.append(item['ID'])
if len(IDs) != 0:
    for ID in IDs:
        sendDelete = req.post(f"{domain}-unsupported/user/{ID}?method=DELETE&apiKey={apiKey}")
else:
    print("No users to delete based on intitial API call")

print('FUNCTION DONE')

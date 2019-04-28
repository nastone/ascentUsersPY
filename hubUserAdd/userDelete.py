import json
import requests as req

fields = 'ID,emailAddr'

username = input('Username>> ')
userPassword = input('Password>> ')

domain = input('Https domain name>> ')
apiKey = input('APIKEY>> ')

login = req.post(f'https://{domain}/attask/api/v10.0/login?username={username}&password={userPassword}')


IDs = []


initGet = req.get(f"https://{domain}/attask/api/v10.0/user/search?entryDate=$$TODAY&apiKey={apiKey}&fields={fields}&$$LIMIT=2000")
response = initGet.json()

data = response
userData = data['data']

for item in userData:
    IDs.append(item['ID'])


if len(IDs) != 0:
    for ID in IDs:
        sendDelete = req.post(f"https://{domain}/attask/api-unsupported/user/{ID}?method=DELETE&apiKey={apiKey}")
else:
    print("No users to delete based on intitial API call")

print('FUNCTION DONE')

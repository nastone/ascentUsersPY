import xlrd
import requests as req
import json
from sys import exit

username = input('Username>> ')
userPassword = input('Password>> ')

domain = input('Https domain name>> ')
apiKey = input('APIKEY>> ')


filePath = input('Past ABSOLUTE file path her for the excel sheet>> ')


login = req.post(f'https://{domain}/attask/api/v10.0/login?username={username}&password={userPassword}')


# example of a filepath for an excel sheet downloaded for Ascent Training
# /Users/rileyrohloff/Downloads/Quicken Loans Wip.xls


loc =(filePath)




userFirstNames = []
userEmail = []
userLastNames = []




wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)
sheet.cell_value(1,0)
#
#
#
# print(sheet.row_values(1))

for i in range(1, sheet.nrows):
    userFirstNames.append(sheet.cell_value(i,0))
    userLastNames.append(sheet.cell_value(i,1))
    userEmail.append(sheet.cell_value(i,3))

    count = len(userEmail)

    user_count = str(count)




for index, item in enumerate(userEmail):
    check_userdata = req.get(f"https://{domain}/attask/api/v10.0/user/search?emailAddr={item}&apiKey={apiKey}")
    userExistQuery = check_userdata.json()
    query = userExistQuery







    if len(query['data']) != 0:
            print(f"{item}, already exists\n\n")
    else:

        updates = {
                    'emailAddr':userEmail[index],
                    'firstName':userFirstNames[index],
                    'lastName':userLastNames[index],
                    'accessLevelID':'7870b41da37bc546e0530a093a0abcf7',
                    'homeGroupID':'5bc8b11500553010367a0ad802d291ff',
                    'password':'Password1'
                    }
        create_call = req.post(f"https://{domain}/attask/api/v10.0/user?updates={updates}&apiKey={apiKey}")
        success = create_call.json()
    if index % 50 == 0:
        print(f"{index} users checked\n")
        print(success)



print("USERS ADDED")

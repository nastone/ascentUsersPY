import xlrd
import requests as req
import json
from sys import exit

apiKey = input('APIKEY>>  ')
domain = input('DOMAIN>>  ')


loc =("/Users/rileyrohloff/Downloads/Quicken Loans Wip.xls")


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


    # print(query['data'])




    if len(query['data']) != 0:
            print(f"{item}, already exists\n\n")
    else:

        updates = {
                    'emailAddr':userEmail[index],
                    'firstName':userFirstNames[index],
                    'lastName':userLastNames[index],
                    'accessLevelID':'56f9863f000fa04b86ccb8f51fb73211',
                    'homeGroupID':'5354d12a001f7b9e8c3f027c727dddb0',
                    'companyID':'4f70af2b000072ad140ec40ea11ea20b',
                    'password':'Password1'
                    }
        create_call = req.post(f"https://{domain}/attask/api/v10.0/user?updates={updates}&apiKey={apiKey}")

    if index % 50 == 0:
        print(f"{index} users checked\n")
        print(query)



print("USERS ADDED")

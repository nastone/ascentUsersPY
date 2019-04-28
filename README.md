# ascentUsersPY
***FOR WORKFRONT USERS ONLY***

This is a public Workfront Inc. repo for CORE TSE's that will allow the TSE to pull down python code that will automate the process of adding users to HUB for Ascent. These .py files will read the excel file given to us by the customer and then create the users in HUB. After that, the TSE will run the verifyUser.py code to verify all the newly created users with a permanent password that will take place the previously used verification step. Instructions for code can be found here: {help article not yet written}. Instructions to download required packages for macOS: {not yet listed}



Instructions:

Firstly, you must have the following python version and packages installed on your local machine:

-Python3.*
-pip (package manager for python packages)
-requests library package
-xlrd (ExcelFile read) package

If you do not have these requirements met, please reach out to Riley and he'll help you get these set up!

Once you have the repository pulled down to your machine, you will be able to automate bulk adding SSO users to HUB for access to Acsent Training (Pretty cool right?!).

Step 1:

'cd' into the directory that you have pulled this repository down too.

Step 2:

From your hubUserAdd directory, run the following command in the command line:

$ python3 addUserFromXL.py

This will pull up the following prompts:

Username>>
PASSWORD>>
DOMAIN>>
APIKEY>>
FILEPATH>> 

You will need to enter in your LDAP credentials and a valid System Admin APIKEY. Then, you will need to paste in the absolute File Path of the Excel file that was provided to you by the customer. (Currently Workfront with CorpIt in getting us a super user for HUB to have API access.)

Once you have entered those credentials, the script will run and will create every user provided in the spreadsheet (as long as they don't have conflicting emails, or already exsist in HUB).

If successfuly run, you should see a '{number} Users Added! SUCCESS' message. If not, please reach out to Riley so he can help troubleshoot.

Step 3:

After you have ran the addUserFromXl script, you need to run the verification script with the following command in the command line:

$ python3 verifyUser.py

This will also ask for you LDAP credentials to HUB and are required for use to log you in. This will automatically verify all the newly created users for that day! If successly, you'll see another 'SUCCESS!' message printed out. 

Please reach out to Riley if you have any further questions.

Good Luck!


import subprocess, os, json
from datetime import date, timedelta

today = date.today()
threedays = today + timedelta(3)
sevendays = today + timedelta(7)
thirtydays = today + timedelta(30)
sixtydays = today + timedelta(60)
toggle = 0

# if there isn't database file, create updated fixture data
if not os.path.isfile("db.sqlite3"):
    # read the fixture data
    with open("dashboard/fixtures/fixtureData.json", "r") as fixtureData:
        data = json.load(fixtureData)
        
    # to test filters, we need the due dates to be relative to the current day, so updateing here
    for i in data:
        if i['model'] == "tasks.task":
            if i["fields"]['due'] == '2023-11-16':
                i["fields"]['due'] = str(today)
            elif i["fields"]['due'] =='2023-11-17':
                i["fields"]['due'] = str(threedays)
            elif i["fields"]['due'] =='2023-11-23':
                i["fields"]['due'] = str(sevendays)
            elif i["fields"]['due'] =='2023-11-19':
                i["fields"]['due'] = str(thirtydays)
            elif i["fields"]['due'] =='2023-11-15':
                i["fields"]['due'] = str(sixtydays)
    
    # save the file
    with open("dashboard/fixtures/updatedFixtureData.json", "w") as fixtureData:
        json.dump(data, fixtureData)
    
    toggle = 1
        
# process the database, after fixure import if that was needed
subprocess.call("python manage.py makemigrations", shell=True)
subprocess.call("python manage.py migrate", shell=True)

if toggle == 1:
    # finally import the new data
    subprocess.call("python manage.py loaddata updatedFixtureData", shell=True)
        

print('\n\n\nuser:     testuser\npassword:     password42069\n\n\n')
# run the server
subprocess.call("python manage.py runserver", shell=True)
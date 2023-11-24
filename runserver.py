import subprocess, os, sqlite3, json
from datetime import date, timedelta

today = date.today()
threedays = today + timedelta(3)
sevendays = today + timedelta(7)
thirtydays = today + timedelta(30)
sixtydays = today + timedelta(60)

# process the database
subprocess.call("python manage.py makemigrations", shell=True)
subprocess.call("python manage.py migrate", shell=True)

# connect to the database and check if a user exists
connection = sqlite3.connect('db.sqlite3')
crsr = connection.cursor()
crsr.execute("SELECT * FROM auth_user")
ans = crsr.fetchall()

# if there isn't a user, then import the fixture data
if len(ans) == 0:
    # read the file
    with open("tasks/fixtures/fixtureData.json", "r") as fixtureData:
        data = json.load(fixtureData)
        
    # to test filters, we need the due dates to be relative to the current day, so updateing here
    for i in data:
        if i['model'] == "tasks.task":
            if i["fields"]['due'] == '2023-11-16':
                i["fields"]['due'] = str(today)
            elif i["fields"]['due'] =='2023-11-17':
                i["fields"]['due'] = str(threedays)
            elif i["fields"]['due'] =='2023-11-18':
                i["fields"]['due'] = str(sevendays)
            elif i["fields"]['due'] =='2023-11-19':
                i["fields"]['due'] = str(thirtydays)
            elif i["fields"]['due'] =='2023-11-15':
                i["fields"]['due'] = str(sixtydays)
    
    # save the file
    with open("tasks/fixtures/updatedFixtureData.json", "w") as fixtureData:
        json.dump(data, fixtureData)
        
    # finally import the new data
    subprocess.call("python manage.py loaddata updatedFixtureData", shell=True)
        

print('\n\n\nuser:     testuser\npassword:     password42069\n\n\n')
# run the server
subprocess.call("python manage.py runserver", shell=True)
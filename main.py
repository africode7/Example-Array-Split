up = "administratoruzi@thispassword288"
splits = up.split("@")

# Extract From Array to String
username = splits[0]
password = splits[1]

print("Username: "+username, "\nPassword: "+password)

print('\n-----------------------------------------------\n')
upall = ["administratoruzi@thispassword288", "adminwp@weak123", "thisusername@thispw"]
# Extract From Array to String + Split Symbol "@"

for extracts in upall:
    splites = extracts.split("@")
    print("Username: "+splites[0])
    print("Password: "+splites[1])
    print('')

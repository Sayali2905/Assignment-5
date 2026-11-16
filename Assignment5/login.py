userid = "admin"
ps = "12345"

count = 1

while (count <= 3):
    user = input("Enter User ID: ")
    password = input("Enter Password: ")

    if (user == userid and password == ps):
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        count = count + 1

if (count > 3):
    print("Maximum attempts reached. Program terminated.")
username = input("Uname ")
password = input("Pword ")
if username.lower() == "admin" and password.lower() == "password123":
    print("Welcome")
else:
    print("access denied")
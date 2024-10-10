age = int(input("Enter age "))
student = input("Are you a student ? Yes/No")
if age < 12 or age >= 65:
    print("£5")
elif student.lower() == "yes":
    print("£8")
else:
    print("£10")
    
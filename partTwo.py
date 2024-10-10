import random
secret_number = random.randint(1 , 10)
x = int(input("Please enter "))
if x >= secret_number:
   print("Too High")
if x <= secret_number:
   print("Too Low")  
if x == secret_number:
   print("Correct")
print(secret_number)
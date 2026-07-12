# WAP to accept 2 numbers from the user and check the greatest

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

if num1 > num2:
    print("Number 1 is the greatest.")
elif num2 > num1:
    print("Number 2 is the greatest.")
else:
    print("Both numbers are equal.")
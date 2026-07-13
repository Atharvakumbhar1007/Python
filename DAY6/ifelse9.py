#1. WAP to check greatest of 2 numbers or both are equal
# Input = 2
# Conditions = 3

n1 = int(input("Enter number 1: ")) 
n2 = int(input("Enter number 2: ")) 

if n1 > n2:
    print(f"n1 = {n1} is greater than n2 = {n2}")
elif n2 > n1:
    print(f"n2 = {n2} is greater than n1 = {n1}")
else:
    print("Both are equal")
# 2. ⁠Simple calculator accept 2 numbers and operator (+,-,*,/) 
# based on operator perform calculations

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

operator = input("Enter operator [+,-,*,/]")

if operator == "+":
    print(f"{n1} + {n2} = {n1+n2}")
elif operator == "-":
    print(f"{n1} - {n2} = {n1-n2}")
elif operator == "*":
    print(f"{n1} * {n2} = {n1*n2}")
elif operator == "/":
    print(f"{n1} / {n2} = {n1/n2}")
else:
    print("Invaid Operator pls enter valid operator")
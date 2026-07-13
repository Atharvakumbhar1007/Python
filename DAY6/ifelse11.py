# WAP to check whether the number is in range 20 to 50 
# or in range -50 to -20

n = int(input("Enter a number: "))

if n >= 20 and n<=50:
    print(f"Number = {n} is in range 20 to 50")

elif n <= -20 and n>=-50:
    print(f"Number = {n} is in range -20 to -50")
else:
    print(f"Number = {n} is not in range 20 to 50")
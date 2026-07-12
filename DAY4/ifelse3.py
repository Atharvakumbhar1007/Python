# WAP to check whether the number is divisible by 5 or not

#Divisible by 5 ->  divide by 5
num = int(input("Enter a number: "))

if num % 5 == 0:
    print(f"Number is Divisible by 5")
else:
    print(f"Number is not Divisible by 5")
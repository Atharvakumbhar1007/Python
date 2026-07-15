# WAP to check whether the number is armstrong number or not

num_str = input("Enter a Number: ")

digits = len(num_str)

num = int(num_str)
i = num
sum = 0
while i != 0:
    remainder = i % 10
    power = remainder ** digits
    sum = sum + power
    i = i // 10
    
if sum == num:
    print(f"Number = {num} is a Armstrong number, sum is {sum}")
else:
    print(f"Number = {num} is not a Armstrong number, sum is {sum}")
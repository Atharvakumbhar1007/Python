# WAP to print sum of digits
# 153 -> 1 + 5 + 3

n = int(input("ENter a number: "))
sum = 0
#  FOR INPUT
i = abs(n) 
#abs= works as changes negative to positive
print(i // 10)
while i != 0:
    remainder = i % 10
    sum = sum + remainder
    i = i // 10
print(f"The sum of digit of {n} is = {sum}")
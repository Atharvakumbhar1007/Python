# FIZZ BUZZ
# WAP to iterate from 1 to n and display msg based on criteria
# if num divisible by 3 and 5 both -> FIZZBUZZ
# if num divisible by 3 -> FIZZ
# if num divisible by 5 -> BUZZ
# if num is not divisible by any  -> num
# n = 100
# 1 2 FIZZ 4 BUZZ FIZZ 7 8 FIZZ BUZZ 11 FIZZ 13 14 FIZZBUZZ ... 

n = int(input("Enter a number: "))

i = 1 

while i <= n:
    if i % 5 == 0 and i % 3 == 0:
        print("FIZZBUZZ") 
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
    i = i + 1
# WAP to print odd sum and even sum from 1 to 20 using one loop
# even sum = 2 + 4 + 6 + ... 20
# odd sum = 1 + 3 + 5 ... 19
# start = 1, stop = 20, gap = 1

odd_sum = 0
even_sum = 0
i = 1

while i <= 20:
    if 1 % 2 == 0:
        # Even -> Add value of i to even sum
        even_sum = even_sum + i
    else:
        # Odd -> Add value of i to odd sum
        odd_sum = odd_sum + i
        
print(f"The odd sum from 1 to 20 is {odd_sum}")
print(f"The even sum from 1 to 20 is {even_sum}")
         
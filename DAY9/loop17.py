# WAP to check whether the number is palindrome or not
# 1441 -> 1441 -> Number 1441 is a palindrome number
# 183 -> 381 -> Number 183 is not a palindrome number

n = int(input("Enter a number: "))

i = n
rev = 0

while i != 0:
    remainder = i % 10
    rev = rev * 10 + remainder
    i = i // 10
    
if rev == n:
    print(f"nUMBER {n} is a palindrome number")
else:
    print(f"Number {n} is a not palindrome number, and reverse number is {rev}")
    
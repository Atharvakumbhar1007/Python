# WAP to check whether the given number is prime or not
# Divisible by 1 and itself only

n = int(input("Enter a number: "))

is_Prime = True    # Assume the number is prime
i = 2

while i < n:
    if n % i == 0:
        is_Prime = False
        break
    i = i + 1

if is_Prime:
    print(f"Number {n} is a prime number")
else:
    print(f"Number {n} is not a prime number")
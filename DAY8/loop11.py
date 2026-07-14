#WAP to print factorial of n

n = int(input("Enter a number: "))

factorial = 1

if n < 0:
    print("Fatorial does not exist for negative number.")
elif n == 0 or n == 1:
    print("Factorial =",1)
else:
    for 1 in range(1, n + 1):
        factorial = factorial * 1
        print("Factorial =",factorial)
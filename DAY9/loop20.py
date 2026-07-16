'''
3. WAP to accept n and iteration (x). Then print table of n till x iteration
# Example n = 6 and x = 5
6 * 1 = 6
.
.
'''
n = int(input("enter a number: "))
x = int(input("Enter number of iterations: "))
i = 1
while i <= x:
    table = i * n
    print(f"{n} * {i} = {table}")
    i = i + 1

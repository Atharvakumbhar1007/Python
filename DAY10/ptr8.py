
n = int(input("Enter rows: "))

i = n 
#ROWS
while i <= n:
    #SPACE
    sp = 1
    while sp <= n - i:
        print(" ", end="")
        sp = sp + 1
    
    # STARS/COLUMNS
    j = 1
    while j <= 2*i - 1:
        print("* ",end="")
        j = j + 1
        
    print()
    i = i - 1
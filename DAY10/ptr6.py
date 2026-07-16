i = 5

#ROWS
while i >= 5:
    #SPACE
    sp = 1
    while sp <= 5 - i:
        print(" ", end="")
        sp = sp + 1
    
    # STARS/COLUMNS
    j = 1
    while j <= i:
        print("* ",end="")
        j = j + 1
        
    print()
    i = i - 1
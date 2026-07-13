#WAP to check whether the triangle is a equilateral, isoceles, scalene
# INPUT = 3
#Equilateral -> All 3 sides are equal -> s1 == s2 || s2 == s3 || s1 == s3
#Isoceles -> Any 2 sides are equal -> s1 == s2 || s2 == s3 || s1 == s3
#Scalene -> No Sides are equal

s1 = int(input("Enter side1: "))
s2 = int(input("Enter side2: "))
s3 = int(input("Enter side3: "))
if s1 > 0 and s2 > 0 and s3 > 0:
    
    if s1 == s2 == s3:
        print("Equilateral Triangle")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Isoceles Triangle")
    else:
        print("Scalenr Triangle")
else:
    print("Invalid Triangle. Side cannot be less than 0")
    
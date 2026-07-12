# WAP to accept marks of 5 subject print sum and average
# Based on average display grades
'''
avg is between 90 to 100 -> A Grade
avg is between 60 to 89 -> B Grade
avg is between 50 to 59 -> C Grade
avg is between 35 to 49 -> D Grade
avg below 35 -> FAIL
'''


s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
s4 = int(input("Enter marks of subject 4: "))
s5 = int(input("Enter marks of subject 5: "))

sum = s1 + s2 + s3 + s4 + s5 
avg = sum / 5

print(f"Total Marks is = {sum}")
print(f"Average Marks is = {avg}")

if avg >= 90:
    print("A Grade")
elif avg >=60:
    print("B Grade")
elif avg >=50:
    print("C Grade")
elif avg >=35:
    print("D Grade")
else:
    print("FAIL")
# WAP to check whether the given year is a leap year or not
# Input = 1
# Condition = 2

'''
1. Leap year repeats after every 4 years -> divisible by 4 ->
year % 4 == 0
'''

year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"Year = {year} is a leap year")
else:
    print(f"Year = {year} is not a leap year")
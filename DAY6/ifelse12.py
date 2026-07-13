# WAP to check whether the given year is a leap year or not
# Input = 1
# Condition = 2

'''
1. Leap year repeats after every 4 years -> divisible by 4 ->
year % 4 == 0

2. Century years (100,200,..1800,2000)
a.Not all century are leap year -> Not divisible by 100
-> year % 100 != 0

                    OR

b.Century years that repeats after every 400 year are leap year
-> Divisible by 400 -> year-> year % 400 == 0
'''

year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"Year = {year} is a leap year")
else:
    print(f"Year = {year} is not a leap year")
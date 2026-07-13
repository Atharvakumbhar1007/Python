'''
Write a program to calculate the electricity bill based on
the following conditions:

- First 100 units      : ₹5 per unit
- Next 100 units       : ₹6 per unit (101–200)
- Above 200 units      : ₹7 per unit

Add a fixed charge of ₹150.
Then add 18% tax on the total amount.
'''

# Accept units consumed from the user
units = int(input("Enter units consumed: "))

# Calculate bill amount based on slabs
if units <= 100:
    bill_amount = units * 5

elif units <= 200:
    bill_amount = (100 * 5) + ((units - 100) * 6)

else:
    bill_amount = (100 * 5) + (100 * 6) + ((units - 200) * 7)

# Add fixed charge
total_without_tax = bill_amount + 150

# Add 18% tax
tax = total_without_tax * 0.18
total_with_tax = total_without_tax + tax

# Display the bill
print("\n------------------------------------------")
print("         ELECTRICITY BILL")
print("------------------------------------------")
print(f"Units Consumed     : {units}")
print(f"Bill Amount        : ₹{bill_amount:.2f}")
print(f"Fixed Charge       : ₹150.00")
print(f"Total Without Tax  : ₹{total_without_tax:.2f}")
print(f"18% Tax            : ₹{tax:.2f}")
print(f"Total Bill         : ₹{total_with_tax:.2f}")
print("------------------------------------------")
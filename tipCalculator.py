# This code takes in the bill amount, the percentage of
# tip you wish to give and number of people the bill should 
# be split into and calculated the final amount need to be paid by 
# each customer.

print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people will split the bill?"))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_head = total_bill / people
final_amt = round(bill_per_head,2)
print(f"Your bill per head is: $ {final_amt}")

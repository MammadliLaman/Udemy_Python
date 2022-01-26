# Make tips calculator
bill = input("Welcome to the tip calculator. What was the total bill? ")
tip_percent = int(input("What percentage tip you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
bill_as_float = float(bill[1:])
tip_amount = bill_as_float * tip_percent/100
bill_after_tip = bill_as_float + tip_amount
amount_per_people = round(bill_after_tip / num_people, 2)
message = f"Each person should pay: ${amount_per_people}"
print(message)
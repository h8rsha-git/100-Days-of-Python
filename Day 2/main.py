print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split_no = int(input("How many people to split the bill? "))
per_pay = (total_bill + total_bill*(tip_percent/100) )/ split_no


print(f"Each person should pay: ${round(per_pay,2)}")